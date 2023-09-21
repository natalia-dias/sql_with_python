import os
import sqlite3

from hstest import CheckResult, StageTest, dynamic_test, TestedProgram

db_name = "investor.db"
table_names = ["companies", "financial"]
files_to_delete = ("investor.db",)
db_created_message = "Database created successfully!"

# values to check in tables
test_data_1 = [
    {
        "companies": [
            ("AAPL", "Apple Inc", "Electronic Technology"),
            ("HON", "Honeywell International Inc.", "Producer Manufacturing"),
            ("BA", "Boeing Company (The)", "Electronic Technology")
        ]
    },
    {
        "financial": [
            ("AAPL", 130795000000, 365817000000, 94680000000, 2279000000000, 68470000000, 350662000000, 67405056180,
             51511000000, 283256943820),
            (
                "HON", 7973000000, 34387000000, 5542000000, 131974000000, 10644000000, 63352000000, 19082242991,
                9774000000,
                44269757009),
            ("BA", 1124000000, 62286000000, None, 74262000000, None, None, None, None, None)
        ]
    }
]

# row count to check in tables
test_data_2 = [
    {
        "companies": [
            (98,)
        ]
    },
    {
        "financial": [
            (98,)
        ]
    }
]


def delete_files(arr):
    for file_name in arr:
        try:
            if os.path.exists(file_name):
                os.remove(file_name)
        except PermissionError:
            return


class InvestorTest(StageTest):
    def after_all_tests(self):
        delete_files(files_to_delete)

    @dynamic_test()
    def test1(self):
        t = TestedProgram()
        output = t.start().strip()
        text = db_created_message
        if output.replace("\n", "") != text.replace("\n", ""):
            return CheckResult.wrong(
                f"Your program should output:\n{text}\ninstead of:\n{output}")
        return CheckResult.correct()

    # testing if database exists
    @dynamic_test()
    def test2(self):
        if not os.path.exists(db_name):
            return CheckResult.wrong(
                f"'{db_name}' does not exist!")
        return CheckResult.correct()

    # testing if tables exist
    @dynamic_test()
    def test3(self):
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        for table in table_names:
            query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}';"
            cur.execute(query)
            r = cur.fetchall()
            if not r or r[0][0] != table:
                conn.close()
                return CheckResult.wrong(f"Table {table} not found!")
        conn.close()
        return CheckResult.correct()

    # testing if rows exist in database
    @dynamic_test(data=test_data_1)
    def test4(self, dict_):
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        for table_name, test_values in dict_.items():
            for item in test_values:
                value = item[0]
                query = f"SELECT * FROM {table_name} WHERE ticker = ?"
                cur.execute(query, (value,))
                rows = cur.fetchall()
                # [print(r) for r in rows]
                if not rows:
                    conn.close()
                    return CheckResult.wrong(f"No data found with {item[0]}!")
                elif len(rows) != 1:
                    conn.close()
                    return CheckResult.wrong(f"Too many result for {item[0]}!")
                elif not (item == rows[0]):
                    conn.close()
                    return CheckResult.wrong(f"{item} content is not equal to {rows[0]}")
        conn.close()
        return CheckResult.correct()

    # testing row count
    @dynamic_test(data=test_data_2)
    def test5(self, dict_):
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        for table_name, test_values in dict_.items():
            for item in test_values:
                query = f"SELECT count(*) FROM {table_name}"
                cur.execute(query)
                rows = cur.fetchall()
                # print(rows, item)
                if not (item == rows[0]):
                    conn.close()
                    return CheckResult.wrong(f"{table_name} table should have {item[0]} rows instead of {rows[0][0]}")

        conn.close()
        return CheckResult.correct()


if __name__ == '__main__':
    InvestorTest().run_tests()
