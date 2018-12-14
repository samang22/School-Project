from pico2d import *
import random
import ID

class Music:
    stage1_bgm = None
    stage2_bgm = None
    door_open_soundeffect = None
    door_close_soundeffect = None
    get_weapon_soundeffect = None
    key_drop_soundeffect = None
    bossroom_bgm = None
    stagechange_bgm = None
    laser_soundeffect = None
    issac_hit1 = None
    issac_hit2 = None
    issac_hit3 = None
    bomb_explosion_soundeffect = None
    tear_shoot_soundeffect = None
    tear_pop_soundeffect = None
    def __init__(self):
        print("Creating Music")
        if Music.stage1_bgm == None: Music.stage1_bgm = load_music('../resource/music/05 The Binding of Isaac Soundtrack Sacrificial in HD.mp3')
        if Music.stage2_bgm == None: Music.stage2_bgm = load_music('../resource/music/13 The Binding of Isaac Soundtrack 4cR1f1c14_ in HD.mp3')
        if Music.door_open_soundeffect == None: Music.door_open_soundeffect = load_music('../resource/music/248_Door_Heavy_Open.mp3')
        if Music.door_close_soundeffect == None: Music.door_close_soundeffect = load_music('../resource/music/249_Door_Heavy_Close.mp3')
        if Music.get_weapon_soundeffect == None: Music.get_weapon_soundeffect = load_music('../resource/music/17_superholy.mp3')
        if Music.key_drop_soundeffect == None: Music.key_drop_soundeffect = load_music('../resource/music/186_Key_drop0.mp3')
        if Music.bossroom_bgm == None: Music.bossroom_bgm = load_music('../resource/music/7669.mp3')
        if Music.stagechange_bgm == None: Music.stagechange_bgm = load_music('../resource/music/319_Whoosh_low1.L.mp3')
        if Music.laser_soundeffect == None: Music.laser_soundeffect = load_music('../resource/music/Laser Gun Sound Effect.mp3')
        if Music.issac_hit1 == None: Music.issac_hit1 = load_music('../resource/music/215_Isaac_Hurt_Grunt0.mp3')
        if Music.issac_hit2 == None: Music.issac_hit2 = load_music('../resource/music/214_Isaac_Hurt_Grunt1.mp3')
        if Music.issac_hit3 == None: Music.issac_hit3 = load_music('../resource/music/213_Isaac_Hurt_Grunt2.mp3')
        if Music.bomb_explosion_soundeffect == None: Music.bomb_explosion_soundeffect = load_music('../resource/music/323_boss1_explosions1.mp3')
        if Music.tear_shoot_soundeffect == None: Music.tear_shoot_soundeffect = load_music('../resource/music/13_Tears_Fire_0.mp3')
        if Music.tear_pop_soundeffect == None: Music.tear_pop_soundeffect = load_music('../resource/music/16_TearImpacts0.mp3')

    def PlayStage1BGM(self):
        Music.stage1_bgm.set_volume(64)
        Music.stage1_bgm.repeat_play()
        pass
    def StopStage1BGM(self):
        Music.stage1_bgm.stop()

    def PlayStage2BGM(self):
        Music.stage2_bgm.set_volume(64)
        Music.stage2_bgm.repeat_play()
    def StopStage2BGM(self):
        Music.stage2_bgm.stop()

    def PlayDoorOpenSound(self):
        Music.door_open_soundeffect.play()
    def PlayDoorCloseSound(self):
        Music.door_close_soundeffect.play()

    def PlayGetWeaponSound(self):
        Music.get_weapon_soundeffect.play()

    def PlayKeyDropSound(self):
        Music.key_drop_soundeffect.play()

    def PlayBossRoomSound(self):
        Music.bossroom_bgm.play()

    def PlayStageChangeSound(self):
        Music.stagechange_bgm.play()

    def PlayLaserShootSound(self):
        Music.laser_soundeffect.play()

    def PlayIssacHitSound(self):
        rand = random.randrange(0, 2 + 1)
        if rand == 0:
            Music.issac_hit1.play()
        elif rand == 1:
            Music.issac_hit2.play()
        if rand == 2:
            Music.issac_hit3.play()
    #def PlayBombFuseSound(self):
    #    self.bomb_fuse_soundeffect.play() 
    def PlayBombExplosionSound(self):
        Music.bomb_explosion_soundeffect.play()
    def PlayTearShootSound(self):
        Music.tear_shoot_soundeffect.play() 
    def PlayTearPopSound(self):
        Music.tear_pop_soundeffect.play() 

    def GetID(self):
        return self.ID

