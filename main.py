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
    def get_most_num_of_wins(self):
        ans=self.cursor.execute("select Champion ,count(*) from Champions group by Champion order by count(*) desc")
        return ans
    def most_no_of_lost_final(self):
        runnerups=self.cursor.execute("select  Runner_Up ,count(*) from Champions group by Runner_Up order by count(*) DESC")
        return runnerups
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
        champ=(self.cursor.execute("select Year, Champion from Champions order by Year"))
        return champ
    def get_mvp(self):
        mvp=self.cursor.execute("select Player_Of_The_Series ,count(*) from Champions group by Player_Of_The_Series order by count(*) DESC")
        return mvp
    def won_home(self):
        chap_home=self.cursor.execute("select Host , count(*) from Champions where Champion=Host group by Host")
        return chap_home
c=champions()
# c.inser_data("champion.csv")
# c.get_most_num_of_wins(c)
# c.most_no_of_lost_final()
# c.no_teams_played()
# print(c.highest_run_scorer())
# print(c.Highest_Wicket_Taker())
# print(c.get_mvp())
# print(c.won_home())
def Champions():
    # get champtio  per years
    year,champion=zip(*c.get_year_champion().fetchall())
    plt.figure(figsize=(50,50))
    plt.subplot(3,2,1)
    plt.plot(year,champion,marker='o',linestyle='-',color='b')
    plt.xlabel('Years')
    plt.ylabel('Champion Team')
    plt.title('Year-wise Champion Distribution')
    plt.grid(True)
    # teams which lost most mnumber of finals
    team,count=zip(*c.most_no_of_lost_final().fetchall())
    plt.subplot(3,2,2)
    plt.bar(team,count,color='orange')
    plt.ylabel("Appears in the Final")
    plt.xlabel("Team")
    plt.title("Most Runner up appearence")
    players,mvp_count=zip(*c.get_mvp().fetchall())
    plt.subplot(3,2,3)
    # player of the tournament
    plt.barh(players,mvp_count,color='green')
    plt.xlabel("Number of Award")
    plt.ylabel("Players")
    plt.title("Most Valuable Players (MVPs)")
    plt.subplot(3,2,4)
    host,wins=zip(*c.won_home().fetchall())
    plt.pie(wins,labels=host,autopct='%0.1f%%') 
    # for win percentage
    teams_win , no_wins =zip(*c.get_most_num_of_wins().fetchall())
    teams_loss=team
    no_loss=count
    final_played={}
    for i in range(len(teams_win)):
        if not teams_win[i] in final_played:
            final_played[teams_win[i]]=no_wins[i]
    for i in range(len(teams_loss)):
        if not teams_loss[i] in final_played:
            final_played[teams_loss[i]]=no_loss[i]
        else:
            final_played[teams_loss[i]]+=no_loss[i]
    win_percent={}
    for i in range(len(teams_win)):
        win_percent[teams_win[i]]=(no_wins[i]/final_played[teams_win[i]])*100
    for i in range(len(teams_loss)):
        if not teams_loss[i] in win_percent:
            win_percent[teams_loss[i]]=100-(no_loss[i]/final_played[teams_loss[i]])*100
    print(win_percent)
    plt.subplot(3,2,5)
    plt.scatter(list(final_played.values()),list(win_percent.values()),c=[10,20,30,40],s=100,cmap='viridis')
    for key ,val in win_percent.items():
        plt.text(final_played[key],val,key,fontsize=12)
    plt.xlabel("Total Finals Played")
    plt.ylabel("Winning Percentage")
    plt.title("Finals Played vs Winning Percentage")
    plt.suptitle("Asia Cup 1984-2022")
    plt.show()

Champions()

