from app import create_app
from app.models import db, Question

app = create_app()

sample_questions = [
    {"content": "현재 작업 중인 디렉토리의 절대 경로를 출력하는 명령어는?", "choices": ["pwd", "cd", "ls", "mkdir"], "answer": 1, "concept": "디렉토리 명령어"},
    {"content": "파일이나 디렉토리의 권한(Permission)을 변경할 때 사용하는 명령어는?", "choices": ["chown", "chmod", "chgrp", "umask"], "answer": 2, "concept": "파일 권한 변경"},
    {"content": "데이터의 중복 저장 없이 스트라이핑(Striping) 기술만 사용하여 I/O 성능을 향상시키는 RAID 레벨은?", "choices": ["RAID 0", "RAID 1", "RAID 5", "RAID 6"], "answer": 1, "concept": "RAID 구성"},
    {"content": "다음 중 압축률이 가장 높은 압축 유틸리티는?", "choices": ["compress", "gzip", "bzip2", "xz"], "answer": 4, "concept": "파일 압축"},
    {"content": "vi 에디터에서 현재 커서가 있는 줄을 삭제하는 명령은?", "choices": ["yy", "dd", "x", "u"], "answer": 2, "concept": "vi 에디터"},
    {"content": "새로운 사용자를 생성할 때 사용하는 명령어는?", "choices": ["useradd", "usermod", "userdel", "passwd"], "answer": 1, "concept": "사용자 관리"},
    {"content": "현재 실행 중인 프로세스의 상태를 트리 형태로 보여주는 명령어는?", "choices": ["ps", "top", "pstree", "jobs"], "answer": 3, "concept": "프로세스 관리"},
    {"content": "특정 프로세스에게 시그널(Signal)을 보내 종료시킬 때 사용하는 명령어는?", "choices": ["stop", "halt", "kill", "exit"], "answer": 3, "concept": "프로세스 종료"},
    {"content": "디스크의 남은 공간을 확인하는 명령어는?", "choices": ["df", "du", "fdisk", "mount"], "answer": 1, "concept": "디스크 용량 확인"},
    {"content": "RPM 패키지를 설치할 때 사용하는 옵션으로 알맞은 것은?", "choices": ["-e", "-q", "-i", "-U"], "answer": 3, "concept": "RPM 패키지 관리"},
    {"content": "데비안 계열 리눅스에서 패키지를 설치하는 명령어는?", "choices": ["yum", "rpm", "apt-get", "tar"], "answer": 3, "concept": "apt-get 패키지 관리"},
    {"content": "네트워크 인터페이스의 IP 주소 및 상태를 확인하거나 설정하는 명령어는?", "choices": ["ping", "netstat", "ifconfig", "route"], "answer": 3, "concept": "네트워크 인터페이스"},
    {"content": "도메인 이름을 IP 주소로 변환해주는 서비스는?", "choices": ["DHCP", "DNS", "FTP", "SSH"], "answer": 2, "concept": "DNS 서비스"},
    {"content": "리눅스에서 기본적으로 사용하는 부트로더는?", "choices": ["LILO", "GRUB", "MBR", "BIOS"], "answer": 2, "concept": "부트로더 GRUB"},
    {"content": "파일의 소유자와 소유 그룹을 한 번에 변경할 수 있는 명령어는?", "choices": ["chmod", "chown", "chgrp", "umask"], "answer": 2, "concept": "소유권 변경"},
    {"content": "파티션을 생성하거나 삭제할 때 사용하는 명령어는?", "choices": ["mkfs", "mount", "fdisk", "df"], "answer": 3, "concept": "파티션 관리"},
    {"content": "시스템 부팅 시 자동으로 마운트될 파일 시스템 정보가 저장된 파일은?", "choices": ["/etc/fstab", "/etc/mtab", "/etc/inittab", "/etc/profile"], "answer": 1, "concept": "fstab 설정"},
    {"content": "원격지 서버에 안전하게 접속하기 위해 암호화된 통신을 제공하는 서비스는?", "choices": ["Telnet", "FTP", "SSH", "HTTP"], "answer": 3, "concept": "SSH 서비스"},
    {"content": "특정 파일이나 디렉토리를 검색할 때 사용하는 명령어는?", "choices": ["find", "grep", "awk", "sed"], "answer": 1, "concept": "find 명령어"},
    {"content": "LVM(Logical Volume Manager) 구성 시 가장 먼저 생성해야 하는 것은?", "choices": ["LV(Logical Volume)", "VG(Volume Group)", "PV(Physical Volume)", "PE(Physical Extent)"], "answer": 3, "concept": "LVM 구성"}
]

with app.app_context():
    # 기존 데이터 모두 지우고 테이블 초기화
    db.drop_all()
    db.create_all()
    
    # 문제 삽입
    for q_data in sample_questions:
        q = Question(
            content=q_data['content'],
            choices=q_data['choices'],
            answer=q_data['answer'],
            concept=q_data['concept']
        )
        db.session.add(q)
    
    db.session.commit()
    print("✅ DB 초기화 및 20문제 삽입 완료!")