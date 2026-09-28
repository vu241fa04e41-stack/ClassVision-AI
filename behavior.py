def analyze_behavior(person_count):


    if person_count == 0:

        return {

        "status":"Empty Classroom",

        "activity":"No Activity"

        }



    if person_count > 60:

        activity="High Activity"

    else:

        activity="Normal Activity"



    return {


        "students":person_count,

        "activity":activity,

        "attention_score":90


    }