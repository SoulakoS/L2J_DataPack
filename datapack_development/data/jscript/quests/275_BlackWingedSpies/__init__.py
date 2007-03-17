# Made by Mr - Version 0.3 by DrLecter
import sys
from net.sf.l2j import Config
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

qn = "275_BlackWingedSpies"

DARKWING_BAT_FANG = 1478
VARANGKAS_PARASITE = 1479
ADENA = 57

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st) :
    htmltext = event
    if event == "30567-03.htm" :
      st.set("cond","1")
      st.setState(STARTED)
      st.playSound("ItemSound.quest_accept")
    return htmltext

 def onTalk (Self,npc,st):
   htmltext = "<html><head><body>I have nothing to say you</body></html>"
   id = st.getState()
   if id == CREATED :
     st.set("cond","0")
   if int(st.get("cond"))==0 :
     if st.getPlayer().getRace().ordinal() != 3 :
       htmltext = "30567-00.htm"
       st.exitQuest(1)
     elif st.getPlayer().getLevel() < 11 :
       htmltext = "30567-01.htm"
       st.exitQuest(1)
     else :
       htmltext = "30567-02.htm"
   else :
     if st.getQuestItemsCount(DARKWING_BAT_FANG) < 70 :
       htmltext = "30567-04.htm"
     else:
       htmltext = "30567-05.htm"
       st.getPcSpawn().removeAllSpawn()
       st.exitQuest(1)
       st.playSound("ItemSound.quest_finish")
       st.giveItems(ADENA,4200)
       st.takeItems(DARKWING_BAT_FANG,-1)
       st.takeItems(VARANGKAS_PARASITE,-1)
   return htmltext

 def onKill (self,npc,st):
   npcId = npc.getNpcId()
   if npcId == 20316 :
     if st.getQuestItemsCount(DARKWING_BAT_FANG) < 70 :
        if st.getQuestItemsCount(DARKWING_BAT_FANG) < 69 :
          st.playSound("ItemSound.quest_itemget")
        else:
          st.playSound("ItemSound.quest_middle")
          st.set("cond","2")
        st.giveItems(DARKWING_BAT_FANG,1)
        if 66>st.getQuestItemsCount(DARKWING_BAT_FANG)>10 and st.getRandom(100) < 10 :
          st.getPcSpawn().addSpawn(27043)
          st.giveItems(VARANGKAS_PARASITE,1)
   else :
      if st.getQuestItemsCount(DARKWING_BAT_FANG) < 66 and st.getQuestItemsCount(VARANGKAS_PARASITE) :
        if st.getQuestItemsCount(DARKWING_BAT_FANG) < 65 :
          st.playSound("ItemSound.quest_itemget")
        else:
          st.playSound("ItemSound.quest_middle")
          st.set("cond","2")
        st.giveItems(DARKWING_BAT_FANG,5)
        st.takeItems(VARANGKAS_PARASITE,-1)
   return

QUEST       = Quest(275,qn,"Black Winged Spies")
CREATED     = State('Start', QUEST)
STARTING    = State('Starting', QUEST)
STARTED     = State('Started', QUEST)
COMPLETED   = State('Completed', QUEST)


QUEST.setInitialState(CREATED)
QUEST.addStartNpc(30567)

CREATED.addTalkId(30567)
STARTING.addTalkId(30567)
STARTED.addTalkId(30567)
COMPLETED.addTalkId(30567)

STARTED.addKillId(20316)
STARTED.addKillId(27043)

STARTED.addQuestDrop(20316,DARKWING_BAT_FANG,1)
STARTED.addQuestDrop(20316,VARANGKAS_PARASITE,1)

print "importing quests: 275: Black Winged Spies"
