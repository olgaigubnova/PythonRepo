from sqlalchemy.sql import text


def test_create_subject_raw_sql(db_session):
    db_session.execute(
        text(
            "INSERT INTO subject (subject_id, subject_title) "
            "VALUES (:id, :title)"
        ),
        {"id": 9001, "title": "Raw SQL Subject"}
    )
    db_session.commit()

    result = db_session.execute(
        text(
            "SELECT subject_title FROM subject "
            "WHERE subject_id = :id"
        ),
        {"id": 9001}
    ).fetchone()

    assert result[0] == "Raw SQL Subject"

    # cleanup
    db_session.execute(
        text(
            "DELETE FROM subject WHERE subject_id = :id"
        ),
        {"id": 9001}
    )
    db_session.commit()


def test_update_subject_raw_sql(db_session):
    db_session.execute(
        text(
            "INSERT INTO subject (subject_id, subject_title) "
            "VALUES (:id, :title)"
        ),
        {"id": 9002, "title": "Old Title"}
    )
    db_session.commit()

    db_session.execute(
        text(
            "UPDATE subject SET subject_title = :title "
            "WHERE subject_id = :id"
        ),
        {"id": 9002, "title": "New Title"}
    )
    db_session.commit()

    result = db_session.execute(
        text(
            "SELECT subject_title FROM subject "
            "WHERE subject_id = :id"
        ),
        {"id": 9002}
    ).fetchone()

    assert result[0] == "New Title"

    # cleanup
    db_session.execute(
        text(
            "DELETE FROM subject WHERE subject_id = :id"
        ),
        {"id": 9002}
    )
    db_session.commit()


def test_delete_subject_raw_sql(db_session):
    db_session.execute(
        text(
            "INSERT INTO subject (subject_id, subject_title) "
            "VALUES (:id, :title)"
        ),
        {"id": 9003, "title": "To Delete"}
    )
    db_session.commit()

    db_session.execute(
        text(
            "DELETE FROM subject WHERE subject_id = :id"
        ),
        {"id": 9003}
    )
    db_session.commit()

    result = db_session.execute(
        text(
            "SELECT subject_id FROM subject "
            "WHERE subject_id = :id"
        ),
        {"id": 9003}
    ).fetchone()

    assert result is None
