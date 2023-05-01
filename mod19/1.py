import sqlite3


def subtask1(cur: sqlite3.Cursor):
    result = cur.execute("""SELECT MAX(avg_grade), teacher_id
                        FROM (SELECT AVG(ag.grade) avg_grade, a.teacher_id teacher_id
                                FROM students s
                                    JOIN assignments_grades ag on s.student_id = ag.student_id
                                    JOIN assignments a on a.assisgnment_id = ag.assisgnment_id
                                GROUP BY a.teacher_id
);
""").fetchone()
    print("Подзадача 1")
    print(*result)


def subtask2(cur: sqlite3.Cursor):
    result = cur.execute("""
    select s.student_id, s.full_name, AVG(ag.grade) avg_grade
        from students s
            join assignments_grades ag on s.student_id = ag.student_id
    group by s.student_id
    order by avg_grade desc
    limit 10;
    """).fetchall()
    print("Подзадача 2")
    for subresult in result:
        print(*subresult)


def subtask3(cur: sqlite3.Cursor):
    result = cur.execute("""
    select s.student_id, s.full_name, sg.teacher_id
    from students s
            join students_groups sg on s.group_id = sg.group_id
    where sg.teacher_id = (
                            select t_id
                            from (select max(avg_grade), t_id
                                    from (select avg(ag.grade) avg_grade, a.teacher_id t_id
                                    from students s
                                            join assignments_grades ag on s.student_id = ag.student_id
                                            join assignments a on a.assisgnment_id = ag.assisgnment_id
                                   group by a.teacher_id
                                   order by avg_grade)));""").fetchall()
    print("Подзадача 3")
    for subresult in result:
        print(*subresult)


def subtask4(cur: sqlite3.Cursor):
    result = cur.execute("""
    select round(avg(count), 3) average, min(count) min_count, max(count) max_count
        from (select count(*) count
                from students s
                    join students_groups sg on s.group_id = sg.group_id
                    join assignments a on sg.group_id = a.group_id
              where (substr(a.due_date, 7) || substr(a.due_date, 4, 2) || substr(a.due_date, 1, 2)) > substr(date(), 7) || substr(date(), 4, 2) || substr(date(), 1, 2)
            group by sg.group_id);
            """).fetchall()[0]
    print("Подзадача 4")
    print(
        f'Среднее количество просроченных заданий: {result[0]},\nМинимальное количество просроченных заданий: {result[1]},\nМаксимальное количество просроченных заданий: {result[2]}')


def subtask5(cur: sqlite3.Cursor):
    pass


def subtask6(cur: sqlite3.Cursor):
    result = cur.execute("""
    select round(avg(ag.grade), 3) as avg_grade
    from assignments a
         join assignments_grades ag on a.assisgnment_id = ag.assisgnment_id
         join students s on ag.student_id = s.student_id
    where a.assignment_text like 'прочитать%' or a.assignment_text like 'выучить%';
    """).fetchone()[0]
    print("Подзадача 6")
    print(result)


def main():
    with sqlite3.connect("homework.sqlite") as con:
        cur = con.cursor()
        subtask1(cur)
        subtask2(cur)
        subtask3(cur)
        subtask6(cur)


if __name__ == '__main__':
    main()
