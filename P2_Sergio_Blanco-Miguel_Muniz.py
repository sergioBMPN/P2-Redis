import redis
db= redis.Redis()
trenes= db.get('trenes')

def trenes_en_marcha(self,*regiones):
    trenes= []
    for region in regiones:
        trenes.append()#añadir trenes.region = region

if __name__ == '__main__':


    val=["val1","val2"]
    #print(*val)
    #db.hset('hash','v1',val)
    #print(db.hget('hash','v1').decode("utf-8"))

    #BRPOP v1 30
    #print(db.brpop("v1",0))

