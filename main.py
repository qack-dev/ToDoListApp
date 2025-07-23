#!/usr/bin/env python3
# -*- coding: shift-jis -*-

# �^�X�N���i�[����ϐ�
tasks = {}
# �^�X�N��ۑ�����t�@�C����
tasks_file = 'tasks.txt'

# �^�X�N��ۑ�����֐�
def save_tasks():
    global tasks
    try:
        with open(tasks_file, 'w') as f:
            f.write(f"{tasks}")
        print("�^�X�N���t�@�C���ɕۑ����܂����B")
    except IOError as e:
        print(f"�t�@�C���̕ۑ��Ɏ��s���܂���: {e}")

# priority�̓��͂𔻒f
def is_priority():
    priority = input("priority: ")
    if priority in ['high', 'middle', 'low']:
        return priority
    else:
        print("priority��'high', 'middle', 'low'�̂����ꂩ����͂��Ă��������B")
        is_priority()

# �^�X�N��ǉ�����֐�
def add():
    global tasks
    # �^�X�N�ƗD��x�̓��͂𑣂�
    print('task����priority(high, middle, low)����͂��Ă��������B')
    task = input("task: ")
    priority = is_priority()
    # �^�X�N�ǉ�
    tasks[len(tasks)] = [task, priority]
    save_tasks()

# �^�X�N���폜�E��������֐��̋��ʕ����̊֐�
def delete():
    for i in range(3):
        num = input("���Ȃ��͓��͂��v2��ԈႦ���܂��B\n> ")
        try:
            num = int(num)
            if num in tasks:
                del tasks[num]
                print(f"�^�X�N {num} ���폜���܂����B")
                save_tasks()
                return
            else:
                print("�����ȃ^�X�N�ԍ��ł��B")
        except ValueError:
            print("���l����͂��Ă��������B")

# �^�X�N���폜����֐�
def remove():
    global tasks
    if not tasks:
        print("�폜����^�X�N������܂���B")
        return
    show()
    print("�폜����^�X�N�ԍ���I��ł��������B")
    delete()

def show():
    global tasks
    if not tasks:
        print("�^�X�N�͂���܂���B")
    else:
        print("���݂̃^�X�N:")
        for key, value in tasks.items():
            print(f"    {key}: {value[0]} (priority: {value[1]})")

# �^�X�N����������֐�
def complete():
    global tasks
    if not tasks:
        print("��������^�X�N������܂���B")
        return
    show()
    print("��������^�X�N�ԍ���I��ł��������B")
    delete()

def main():
    # ���ꂩ��O���[�o���ϐ���ύX���邱�Ƃ�錾
    global tasks
    # �^�X�N��ǂݍ���
    with open(tasks_file, 'r') as f:
        tasks = f.read()
    # �^�X�N�������ɕϊ�
    tasks = eval(tasks) if tasks else {}
    # �������b�Z�[�W
    a = input('�^�X�N�����:add,\n�^�X�N���폜:remove,\n�^�X�N��\��:show,\n�^�X�N������:complete,\n�I��:exit\n> ')
    # ��������
    match a:
        case 'add':
            add()
        case 'remove':
            remove()
        case 'show':
            show()
        case 'complete':
            complete()
        case 'exit':
            print('�I�����܂��B')
            exit()
        case _:
            print("�����ȃR�}���h�ł��B'add', 'remove', 'show', 'complete', 'exit' �̂����ꂩ����͂��Ă��������B")
    main()

if __name__ == '__main__':
	main()
