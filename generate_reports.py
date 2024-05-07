import argparse
import csv
from datetime import datetime

STUDENT_DATA = {
    "9412011005": {"name": "Krasimir Petrov", "credit": 25},
    "9501011014": {"name": "Elena Foteva", "credit": 45},
    "9507141009": {"name": "Ivan Ivanov", "credit": 30}
}

COURSE_DATA = {
    1: {"name": "Analysis", "total_time": 20, "credit": 10, "instructor_name": "Neno Dimitrov"},
    2: {"name": "Linear Algebra", "total_time": 30, "credit": 15, "instructor_name": "Neno Dimitrov"},
    3: {"name": "Statistics", "total_time": 30, "credit": 15, "instructor_name": "Petko Valchev"},
    4: {"name": "Geometry", "total_time": 35, "credit": 20, "instructor_name": "Petar Penchev"}
}

STUDENT_COURSES_DATA = {
    ("9412011005", 1): {"completion_date": "2019-07-16"},
    ("9412011005", 2): {"completion_date": "2019-08-20"},
    ("9501011014", 1): {"completion_date": "2019-07-16"},
    ("9501011014", 2): {"completion_date": "2019-08-01"},
    ("9501011014", 3): {"completion_date": "2019-10-01"},
    ("9501011014", 4): {"completion_date": "2019-12-05"},
    ("9507141009", 4): {"completion_date": "2019-08-20"}
}

def generate_reports(student_pins, min_credit, start_date, end_date, output_format, output_dir):
    if output_format == "csv":
        report_file = open(f"{output_dir}/report.csv", "w", newline="")
        writer = csv.writer(report_file)
        writer.writerow(["Student Name", "Total Credit", "Course Name", "Total Time", "Credit", "Instructor Name"])
    elif output_format == "html":
        report_file = open(f"{output_dir}/report.html", "w")
        report_file.write("<html><body>")

    for pin, student_info in STUDENT_DATA.items():
        if student_pins is None or pin in student_pins:
            total_credit = 0
            student_courses = STUDENT_COURSES_DATA.get(pin, {})

            for course_id, course_data in student_courses.items():
                completion_date = datetime.strptime(course_data["completion_date"], "%Y-%m-%d").date()
                if start_date <= completion_date <= end_date:
                    total_credit += COURSE_DATA[course_id]["credit"]

            if total_credit >= min_credit:
                if output_format == "csv":
                    writer.writerow([student_info["name"], total_credit])
                elif output_format == "html":
                    report_file.write(f"<h2>{student_info['name']}, {total_credit}</h2>")

                for course_id, course_data in student_courses.items():
                    completion_date = datetime.strptime(course_data["completion_date"], "%Y-%m-%d").date()
                    if start_date <= completion_date <= end_date:
                        course_info = COURSE_DATA[course_id]
                        if output_format == "csv":
                            writer.writerow(["", "", course_info["name"], course_info["total_time"], course_info["credit"], course_info["instructor_name"]])
                        elif output_format == "html":
                            report_file.write(f"<p>{course_info['name']}, {course_info['total_time']}, {course_info['credit']}, {course_info['instructor_name']}</p>")

    if output_format == "html":
        report_file.write("</body></html>")

    report_file.close()
    print("Reports generated successfully.")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--student-pins", type=str)
    parser.add_argument("min_credit", type=int)
    parser.add_argument("start_date", type=str)
    parser.add_argument("end_date", type=str)
    parser.add_argument("--output-format", choices=["csv", "html"], default=None)
    parser.add_argument("output_dir", type=str)
    args = parser.parse_args()

    student_pins = args.student_pins.split(",") if args.student_pins else None
    min_credit = args.min_credit
    start_date = datetime.strptime(args.start_date, "%Y-%m-%d")
    end_date = datetime.strptime(args.end_date, "%Y-%m-%d")
    output_format = args.output_format
    output_dir = args.output_dir

    generate_reports(student_pins, min_credit, start_date, end_date, output_format, output_dir)

if __name__ == "__main__":
    main()
