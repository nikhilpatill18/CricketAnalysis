import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
class champions:
    def __init__(self,db="cricket.db"):
        self.conn=sqlite3.connect(db)
        self.cursor=self.conn.cursor()
        self.create_table()
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Champions (
    Year INTEGER PRIMARY KEY,
    Host TEXT,
    No_of_Team INTEGER,
    Champion TEXT,
    RunnerUp TEXT,
    Player_of_Series TEXT,
    Highest_Run_Scorer TEXT,
    Highest_Wicket_Taker TEXT)''')
        self.conn.commit()
    def inser_data(self,filename):
        data=pd.read_csv(filename)
        data.to_sql("Champions",self.conn,if_exists="replace",index=False)
        print("data inserted sucessfully")
    def get_all_chaptions(self):
        ans=self.cursor.execute("select * from Champions")
        # print(ans.fetchall())
        # df=pd.read_sql("select * from Champions where Year='1984'",self.conn)
        return ans.fetchall()
    @staticmethod
    def get_most_num_of_wins(obj):
        teams=[]
        counts=[]
        ans=obj.cursor.execute("select Champion from Champions group by Champion").fetchall()
        for an in ans:
            teams.append(an[0])
        count=obj.cursor.execute("select count(Champion) from Champions group by champion").fetchall()
        for c in count:
            counts.append(c[0])
        plt.bar(teams,counts)
        plt.show()
    def most_no_of_lost_final(self):
        teams=[]
        counts=[]
        ans=self.cursor.execute("select  Runner_Up from Champions group by Runner_Up").fetchall()
        count=self.cursor.execute("select  count(Runner_Up) from Champions group by Runner_Up").fetchall()
        for a in ans:
            teams.append(a[0])
        for c in count:
            counts.append(c[0])
        print(teams,counts)
    def no_teams_played(self):
        year=self.cursor.execute("select Year, No_Of_Team from Champions").fetchall()
        print(year)
    def highest_run_scorer(self):
        mostruns=self.cursor.execute("select Highest_Run_Scorer ,count(*) from Champions group by Highest_Run_Scorer").fetchall()
        return mostruns
    def Highest_Wicket_Taker(self):
        mostwicket=self.cursor.execute("select Highest_Wicket_Taker ,count(*) from Champions group by Highest_Wicket_Taker").fetchall()
        return mostwicket
    def get_year_champion(self):
        champ=self.cursor.execute("select Year, Champion from Champions order by Year").fetchall()
        return champ




c=champions()
# c.inser_data("champion.csv")
# c.get_most_num_of_wins(c)
c.most_no_of_lost_final()
c.no_teams_played()
print(c.highest_run_scorer())
print(c.Highest_Wicket_Taker())

