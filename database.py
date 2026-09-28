import sqlite3



connection = sqlite3.connect(

"classroom.db",

check_same_thread=False

)



cursor = connection.cursor()



cursor.execute("""


CREATE TABLE IF NOT EXISTS attendance(

id INTEGER PRIMARY KEY,

classroom TEXT,

students INTEGER,

attendance REAL

)


""")



connection.commit()





def save_data(room,students,attendance):


    cursor.execute(

    """

    INSERT INTO attendance

    (classroom,students,attendance)

    VALUES(?,?,?)

    """,

    (

    room,

    students,

    attendance

    )


    )


    connection.commit()