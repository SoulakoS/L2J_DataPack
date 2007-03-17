# Maked by Mr. Have fun! Version 0.2
# Updated by ElgarL

import sys
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

qn = "401_PathToWarrior"

EINS_LETTER_ID = 1138
WARRIOR_GUILD_MARK_ID = 1139
RUSTED_BRONZE_SWORD1_ID = 1140
RUSTED_BRONZE_SWORD2_ID = 1141
SIMPLONS_LETTER_ID = 1143
POISON_SPIDER_LEG2_ID = 1144
MEDALLION_OF_WARRIOR_ID = 1145
RUSTED_BRONZE_SWORD3_ID = 1142

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st) :
    htmltext = event
    if event == "401_1" :
          if st.getPlayer().getClassId().getId() == 0x00 :
            if st.getPlayer().getLevel() >= 19 :
              if st.getQuestItemsCount(MEDALLION_OF_WARRIOR_ID)>0 :
                htmltext = "30010-04.htm"
              else:
                htmltext = "30010-05.htm"
                return htmltext
            else :
              htmltext = "30010-02.htm"
          else:
            if st.getPlayer().getClassId().getId() == 0x01 :
              htmltext = "30010-02a.htm"
            else:
              htmltext = "30010-03.htm"
    elif event == "401_2" :
          htmltext = "30010-10.htm"
    elif event == "401_3" :
            htmltext = "30010-11.htm"
            st.takeItems(SIMPLONS_LETTER_ID,1)
            st.takeItems(RUSTED_BRONZE_SWORD2_ID,1)
            st.giveItems(RUSTED_BRONZE_SWORD3_ID,1)
            st.set("cond","5")
    elif event == "1" :
      st.set("id","0")
      if st.getQuestItemsCount(EINS_LETTER_ID) == 0 :
        st.set("cond","1")
        st.setState(STARTED)
        st.playSound("ItemSound.quest_accept")
        st.giveItems(EINS_LETTER_ID,1)
        htmltext = "30010-06.htm"
    elif event == "30253_1" :
          htmltext = "30253-02.htm"
          st.takeItems(EINS_LETTER_ID,1)
          st.giveItems(WARRIOR_GUILD_MARK_ID,1)
          st.set("cond","2")
    return htmltext


 def onTalk (Self,npc,st):

   npcId = npc.getNpcId()
   htmltext = "<html><head><body>I have nothing to say you</body></html>"
   id = st.getState()
   if id == CREATED :
     st.setState(STARTING)
     st.set("cond","0")
     st.set("onlyone","0")
     st.set("id","0")
   if npcId == 30010 and int(st.get("cond"))==0 :
      htmltext = "30010-01.htm"
   elif npcId == 30010 and int(st.get("cond")) and st.getQuestItemsCount(EINS_LETTER_ID)>0 :
      htmltext = "30010-07.htm"
   elif npcId == 30010 and int(st.get("cond")) and st.getQuestItemsCount(WARRIOR_GUILD_MARK_ID)==1 :
      htmltext = "30010-08.htm"
   elif npcId == 30253 and int(st.get("cond")) and st.getQuestItemsCount(EINS_LETTER_ID) :
      htmltext = "30253-01.htm"
   elif npcId == 30253 and int(st.get("cond")) and st.getQuestItemsCount(WARRIOR_GUILD_MARK_ID) :
      if st.getQuestItemsCount(RUSTED_BRONZE_SWORD1_ID)<1 :
        htmltext = "30253-03.htm"
      elif st.getQuestItemsCount(RUSTED_BRONZE_SWORD1_ID)<10 :
        htmltext = "30253-04.htm"
      elif st.getQuestItemsCount(RUSTED_BRONZE_SWORD1_ID) >= 10 :
        st.takeItems(WARRIOR_GUILD_MARK_ID,1)
        st.takeItems(RUSTED_BRONZE_SWORD1_ID,st.getQuestItemsCount(RUSTED_BRONZE_SWORD1_ID))
        st.giveItems(RUSTED_BRONZE_SWORD2_ID,1)
        st.giveItems(SIMPLONS_LETTER_ID,1)
        st.set("cond","4")
        htmltext = "30253-05.htm"
   elif npcId == 30253 and int(st.get("cond")) and st.getQuestItemsCount(SIMPLONS_LETTER_ID) :
        htmltext = "30253-06.htm"
   elif npcId == 30010 and int(st.get("cond")) and st.getQuestItemsCount(SIMPLONS_LETTER_ID) and st.getQuestItemsCount(RUSTED_BRONZE_SWORD2_ID) and st.getQuestItemsCount(WARRIOR_GUILD_MARK_ID)==0 and st.getQuestItemsCount(EINS_LETTER_ID)==0 :
        htmltext = "30010-09.htm"
   elif npcId == 30010 and int(st.get("cond")) and st.getQuestItemsCount(RUSTED_BRONZE_SWORD3_ID) and st.getQuestItemsCount(WARRIOR_GUILD_MARK_ID)==0 and st.getQuestItemsCount(EINS_LETTER_ID)==0 :
        if st.getQuestItemsCount(POISON_SPIDER_LEG2_ID)<20 :
          htmltext = "30010-12.htm"
        elif st.getQuestItemsCount(POISON_SPIDER_LEG2_ID)>19 :
          st.takeItems(POISON_SPIDER_LEG2_ID,st.getQuestItemsCount(POISON_SPIDER_LEG2_ID))
          st.takeItems(RUSTED_BRONZE_SWORD3_ID,1)
          st.giveItems(MEDALLION_OF_WARRIOR_ID,1)
          htmltext = "30010-13.htm"
          st.set("cond","0")
          st.setState(COMPLETED)
          st.playSound("ItemSound.quest_finish")
   return htmltext

 def onKill (self,npc,st):

   npcId = npc.getNpcId()
   if npcId in [20035,20042] :
        st.set("id","0")
        if int(st.get("cond")) == 2 and st.getQuestItemsCount(RUSTED_BRONZE_SWORD1_ID)<10 :
          if st.getRandom(10)<4 :
            st.giveItems(RUSTED_BRONZE_SWORD1_ID,1)
            if st.getQuestItemsCount(RUSTED_BRONZE_SWORD1_ID) == 10 :
              st.playSound("ItemSound.quest_middle")
              st.set("cond","3")
            else:
              st.playSound("ItemSound.quest_itemget")
   elif npcId in [20043,20038] :
      st.set("id","0")
      if int(st.get("cond")) and st.getQuestItemsCount(POISON_SPIDER_LEG2_ID)<20 and st.getQuestItemsCount(RUSTED_BRONZE_SWORD3_ID) == 1 and st.getItemEquipped(7) == RUSTED_BRONZE_SWORD3_ID:
        st.giveItems(POISON_SPIDER_LEG2_ID,1)
        if st.getQuestItemsCount(POISON_SPIDER_LEG2_ID) == 20 :
          st.playSound("ItemSound.quest_middle")
          st.set("cond","6")
        else:
          st.playSound("ItemSound.quest_itemget")

   return

QUEST       = Quest(401,qn,"Path To Warrior")
CREATED     = State('Start', QUEST)
STARTING     = State('Starting', QUEST)
STARTED     = State('Started', QUEST)
COMPLETED   = State('Completed', QUEST)


QUEST.setInitialState(CREATED)
QUEST.addStartNpc(30010)

STARTING.addTalkId(30010)

STARTED.addTalkId(30010)
STARTED.addTalkId(30253)

STARTED.addKillId(20035)
STARTED.addKillId(20038)
STARTED.addKillId(20042)
STARTED.addKillId(20043)

STARTED.addQuestDrop(30253,SIMPLONS_LETTER_ID,1)
STARTED.addQuestDrop(30253,RUSTED_BRONZE_SWORD2_ID,1)
STARTED.addQuestDrop(30010,EINS_LETTER_ID,1)
STARTED.addQuestDrop(30253,WARRIOR_GUILD_MARK_ID,1)
STARTED.addQuestDrop(20035,RUSTED_BRONZE_SWORD1_ID,1)
STARTED.addQuestDrop(20042,RUSTED_BRONZE_SWORD1_ID,1)
STARTED.addQuestDrop(20043,POISON_SPIDER_LEG2_ID,1)
STARTED.addQuestDrop(20038,POISON_SPIDER_LEG2_ID,1)
STARTED.addQuestDrop(30010,RUSTED_BRONZE_SWORD3_ID,1)
print "importing quests: 401: Path To Warrior"