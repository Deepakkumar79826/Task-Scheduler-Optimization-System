import csv

class ReportGenerator:

    @staticmethod
    def generate_csv(schedule):

        with open(
            "outputs/schedule_report.csv",
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow(
                ["Task", "Start", "End"]
            )

            start = 0

            for task in schedule:

                end = start + task.execution_time

                writer.writerow(
                    [task.name, start, end]
                )

                start = end

    @staticmethod
    def generate_text(
        schedule,
        missed,
        total_profit
    ):

        with open(
            "outputs/schedule_report.txt",
            "w"
        ) as file:

            file.write(
                "TASK SCHEDULER REPORT\n\n"
            )

            file.write(
                "Scheduled Tasks\n"
            )

            for task in schedule:

                file.write(
                    f"{task.name}\n"
                )

            file.write(
                "\nMissed Tasks\n"
            )

            for task in missed:

                file.write(
                    f"{task.name}\n"
                )

            file.write(
                f"\nTotal Profit: {total_profit}"
            )