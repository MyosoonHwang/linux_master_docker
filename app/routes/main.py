from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models import db, Question, WrongAnswer
from app.services.gemini_service import get_wrong_answer_explanation

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    # 405 에러 해결: POST 요청이 들어오면 바로 시험지로 보냅니다.
    if request.method == 'POST':
        return redirect(url_for('main.exam'))
    return render_template('index.html')

@main_bp.route('/start_exam', methods=['POST', 'GET'])
def start_exam():
    # 404 에러 해결: 기존 html의 formaction 흔적이 남아있어도 무조건 시험지로 보냅니다.
    return redirect(url_for('main.exam'))

@main_bp.route('/exam')
def exam():
    # DB에 고정된 20문제를 가져옵니다.
    questions = Question.query.all()
    if not questions:
        return "DB에 문제가 없습니다. 터미널에서 'python seed_db.py'를 먼저 실행해주세요.", 400
    return render_template('exam.html', questions=questions)

@main_bp.route('/submit', methods=['POST'])
def submit():
    questions = Question.query.all()
    
    for q in questions:
        user_ans = request.form.get(f'q_{q.id}')
        # 오답인 경우에만 DB 저장
        if not user_ans or int(user_ans) != q.answer:
            new_wrong = WrongAnswer(
                content=q.content,
                choices=q.choices,
                correct_answer=q.answer,
                user_answer=int(user_ans) if user_ans else 0,
                concept=q.concept
            )
            db.session.add(new_wrong)
            
    db.session.commit()
    return redirect(url_for('main.review'))

@main_bp.route('/review')
def review():
    wrongs = WrongAnswer.query.order_by(WrongAnswer.created_at.desc()).all()
    return render_template('review.html', wrongs=wrongs)

@main_bp.route('/api/explain/<int:wrong_id>', methods=['POST'])
def explain_wrong_answer(wrong_id):
    # AI 해설용 API
    wrong = WrongAnswer.query.get_or_404(wrong_id)
    correct_text = wrong.choices[wrong.correct_answer - 1]
    user_text = wrong.choices[wrong.user_answer - 1] if wrong.user_answer > 0 else "선택 안 함"
    explanation = get_wrong_answer_explanation(wrong.content, correct_text, user_text)
    return jsonify({"explanation": explanation})