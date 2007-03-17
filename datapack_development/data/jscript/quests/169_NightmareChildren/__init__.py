# Maked by Mr. Have fun! Version 0.2
print "importing quests: 169: Nightmare Children"
import sys
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

qn = "169_NightmareChildren"

CRACKED_SKULL_ID = 1030
PERFECT_SKULL_ID = 1031
BONE_GAITERS_ID = 31

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st) :
    htmltext = event
    if event == "1" :
      st.set("id","0")
      htmltext = "30145-04.htm"
      st.set("cond","1")
      st.setState(STARTED)
      st.playSound("ItemSound.quest_accept")
    elif event == "169_1" and int(st.get("onlyone")) == 0 :
          if int(st.get("id")) != 169 :
            st.set("id","169")
            htmltext = "30145-08.htm"
            st.giveItems(BONE_GAITERS_ID,1)
            st.giveItems(57,17150)
            st.takeItems(CRACKED_SKULL_ID,st.getQuestItemsCount(CRACKED_SKULL_ID))
            st.takeItems(PERFECT_SKULL_ID,st.getQuestItemsCount(PERFECT_SKULL_ID))
            st.set("cond","0")
            st.setState(COMPLETED)
            st.playSound("ItemSound.quest_finish")
            st.set("onlyone","1")
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
   if npcId == 30145 and int(st.get("cond"))==0 and int(st.get("onlyone"))==0 :
      if int(st.get("cond"))<15 :
        if st.getPlayer().getRace().ordinal() != 2 :
          htmltext = "30145-00.htm"
        elif st.getPlayer().getLevel() >= 15 :
          htmltext = "30145-03.htm"
          return htmltext
        else:
          htmltext = "30145-02.htm"
          st.exitQuest(1)
      else:
        htmltext = "30145-02.htm"
        st.exitQuest(1)
   elif npcId == 30145 and int(st.get("cond"))==0 and int(st.get("onlyone"))==1 :
      htmltext = "<html><head><body>This quest have already been completed.</body></html>"
   elif npcId == 30145 and int(st.get("cond")) :
      if st.getQuestItemsCount(CRACKED_SKULL_ID) >= 1 and st.getQuestItemsCount(PERFECT_SKULL_ID) == 0 :
        htmltext = "30145-06.htm"
      elif st.getQuestItemsCount(PERFECT_SKULL_ID) >= 1 :
          htmltext = "30145-07.htm"
      elif st.getQuestItemsCount(CRACKED_SKULL_ID) == 0 and st.getQuestItemsCount(PERFECT_SKULL_ID) == 0 :
          htmltext = "30145-05.htm"
   return htmltext

 def onKill (self,npc,st):

   npcId = npc.getNpcId()
   if npcId == 20105 :
      st.set("id","0")
      if int(st.get("cond")) == 1 :
        if st.getRandom(10)>7 and st.getQuestItemsCount(PERFECT_SKULL_ID) == 0 :
          st.giveItems(PERFECT_SKULL_ID,1)
          st.playSound("ItemSound.quest_middle")
        if st.getRandom(10)>4 :
          st.giveItems(CRACKED_SKULL_ID,1)
          st.playSound("ItemSound.quest_itemget")
   elif npcId == 20025 :
      st.set("id","0")
      if int(st.get("cond")) == 1 :
        if st.getRandom(10)>7 and st.getQuestItemsCount(PERFECT_SKULL_ID) == 0 :
          st.giveItems(PERFECT_SKULL_ID,1)
          st.playSound("ItemSound.quest_middle")
        if st.getRandom(10)>4 :
          st.giveItems(CRACKED_SKULL_ID,1)
          st.playSound("ItemSound.quest_itemget")
   return

QUEST       = Quest(169,qn,"Nightmare Children")
CREATED     = State('Start', QUEST)
STARTING     = State('Starting', QUEST)
STARTED     = State('Started', QUEST)
COMPLETED   = State('Completed', QUEST)


QUEST.setInitialState(CREATED)
QUEST.addStartNpc(30145)

STARTING.addTalkId(30145)

STARTED.addTalkId(30145)

STARTED.addKillId(20105)
STARTED.addKillId(20025)

STARTED.addQuestDrop(20105,CRACKED_SKULL_ID,1)
STARTED.addQuestDrop(20025,CRACKED_SKULL_ID,1)
STARTED.addQuestDrop(20105,PERFECT_SKULL_ID,1)
STARTED.addQuestDrop(20025,PERFECT_SKULL_ID,1)
