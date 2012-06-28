import datetime
#
#Match Class
#
class Match:
    def __init__(self,hometeam,awayteam,matchdate,homescores=None,awayscores=None):
        self.home_team=hometeam
        self.away_team=awayteam
        self.date=matchdate
        self.home_scores={}
        self.away_scores={}

    def add_score(self,player,goal):
        
        if(player=="Torres"):
            if player in self.home_scores:
                while player:
                    newvalue=self.home_scores.values()
                    oldvalue=int(newvalue[0])
                    newgoal=oldvalue+goal
                    self.home_scores[player]=newgoal
                    print self.home_scores.items()
                    break
            else:
                self.home_scores[player]=goal
                print self.home_scores.items()
        else:
            self.away_scores[player]=goal
            print self.away_scores.items()

    def home_score(self):
        for playerkey in self.home_scores:
            goals=self.home_scores.values()
            totalgoals=sum(goals)
            if totalgoals==0:
                return totalgoals
            else:
                print self.home_team,": ", totalgoals

    def away_score(self):
        for plyerkey in self.away_scores:
            awaygoals=self.away_scores.values()
            totalawaygoals=sum(awaygoals)
            if totalawaygoals==0:
                return totalawaygoals
            else:
                print self.away_team,": ", totalawaygoals

    def winner(self):
        
        homegoalscored=self.home_scores.values()
        hgoals=sum(homegoalscored)

        awaygoalsscored=self.away_scores.values()
        agoals=sum(awaygoalsscored)

        if(hgoals>agoals):
            print self.home_team," is the winner"
        elif (hgoals==agoals):
            print self.away_team, "won the game"
            

    #def away_score(self):


#
#player class
#

        
class player:
    def __init__(self,fname_val,lname_val,team=None):        
        self.first_name=fname_val
        self.last_name=lname_val
        self.scores=[]
        self.team=team

    def add_score(self,score):
                 
        self.scores.append(score)
        print self.scores
        #print var
        #print self.scores()

    def total_score(self):
        total=sum(self.scores)
        print self.last_name, "Total number of goals: ",total

    def average_score(self):
        avg=(sum(self.scores))/len(self.scores)
        print self.last_name, "Average number of goals: ", avg
        




#
#Team Class
#
class Team:
    portugal="Portugal"
    spain="Spain"
    def __init__(self,name,league,manager_name,points,players=None):
        self.TeamName=name
        self.MajorLeague=league
        self.Manager=manager_name
        self.pts=points
        self.players=[]
      

    def add_player(self,player):
        
        self.players.append(player)
        print self.players
        #print player,"plays for", team
        
    def __str__(self):
        
            printout=self.TeamName+" plays in the "+self.MajorLeague+" League\n and is managed by "+self.Manager+". \n The Team has obtained "+self.pts
            return printout


#accepts details of team
teamname=raw_input("Enter name of team: ")
lge=raw_input("League: ")
mgr=raw_input("Manager Name: ")
ptrs=raw_input("Points obtained: ")
playerlist=raw_input("Player List: ")
myTeam=Team(teamname,lge,mgr,ptrs,playerlist)

#This accpets the attribute values from the user
fname=raw_input("Enter FirstName: ")
lname=raw_input("Enter LastName: ")
Team=myTeam.spain #assigns player to team spain
#torres is now an insatnace of the player class
torres=player(fname,lname,Team)
#torres.add_score(3)
print ".................End of Torres............."
fname=raw_input("Enter FirstName: ")
lname=raw_input("Enter LastName: ")
Team=myTeam.portugal #assigns player to team portugal
#torres is now an insatnace of the player class
ronaldo=player(fname,lname,Team)
print ".................End of Ronaldo............."

#adding a player to the team
myTeam.add_player(torres.last_name)
myTeam.add_player(ronaldo.last_name)
print "Player list", myTeam
#print myTeam

print "................Players added to team............."


#accepts match date
yr=int(raw_input("Enter match Year: "))
month=int(raw_input("Enter match Month: "))
day=int(raw_input("Enter match Day: "))


#accepts first home player who scored
HomePlayer=raw_input("Home Player who scored: ")
Homegoal=int(raw_input("Enter goal: "))
#homescore={}
#awayscore={}

matchdate=datetime.date(yr,month,day)

#mymaatch creates an instance of the Match class
mymatch=Match(myTeam.spain,myTeam.portugal,matchdate)

#calls the add_score function and passes player and score values
mymatch.add_score(HomePlayer,Homegoal)
print ".......First Home Goal Recorded........"
#accepts first away player who scored
AwayPlayer=raw_input("Away Player who scored: ")
Awaygoal=int(raw_input("Enter goal: "))

mymatch.add_score(AwayPlayer,Awaygoal)
print ".......First Away Goal Recorded........"


#accepts second home player who scored
HomePlayer2=raw_input("Home Player who scored: ")
Homegoal2=int(raw_input("Enter goal: "))
mymatch.add_score(HomePlayer2,Homegoal2)
print ".......Secon Home Goal Recorded........"

mymatch.home_score()
mymatch.away_score()
mymatch.winner()


'''
num_score=int(raw_input("Enter Number of score: "))
print "....................................."
n=0
while n<num_score:
    newscore=int(raw_input("Enter Score: "))
    torres.add_score(newscore)
    n=n+1
    if n>=num_score:
        
        break

torres.total_score()
torres.average_score()
'''

#self.team=score
#print self.team
#num_score=int(raw_input("Enter Number of score: "))
#n=0
#while n<num_score:
