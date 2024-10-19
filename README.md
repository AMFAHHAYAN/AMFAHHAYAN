



Task: Marksheet Calculation using Django
You are required to create a Django-based web application to input marks for different subjects and generate a marksheet. The task is divided into the following steps:
    1. Create a form where the user can input the following for each subject:
        ◦ Subject Name
        ◦ Theory Marks (out of 80)
        ◦ Internal Assessment Marks (out of 20)
    2. Perform the following calculations:
        ◦ Calculate the total marks for each subject by adding the theory and internal assessment marks.
        ◦ Calculate the percentage.
        ◦ Determine if the student has passed or failed each subject based on the following rule:
            ▪ A student passes a subject if their total marks (Theory + Internal) are 35 or more.
    3. Display the marksheet:
        ◦ The marksheet should display the subject name, theory marks, internal assessment marks, total marks, and pass/fail status for each subject.
        ◦ At the bottom, display the total marks obtained by the student out of the maximum possible marks and indicate if the student has passed or failed overall.
            ▪ A student passes overall if they pass in all subjects.
    4. Add a logical component:
        ◦ Implement a rule where if a student fails in one subjects, the overall result should be "Fail" even if they have passed in some subjects.
Requirements:
    • Create a Django model to store the marks data.
    • Use HTML forms for input.
    • Perform the necessary calculations in the views.
    • Use Django templates to display the marksheet in a format similar to a traditional marksheet.







The UI of the HTML Page should be something like this. Use HTML Tables to achieve the UI.
