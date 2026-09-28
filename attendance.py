def calculate_attendance(

    total_students,

    present_students

):


    if total_students==0:

        return 0



    percentage=(

        present_students /

        total_students

    )*100



    return round(

        percentage,2

    )