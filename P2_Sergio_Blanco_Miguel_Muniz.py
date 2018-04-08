import redis

r = redis.Redis(host='localhost', port=6379)

def consultarTramos(via):
    if(r.hlen(via) == 0):
        raise ("La via que intenta consultar no existe")

    tramos = r.hkeys(via)
    estados = r.hvals(via)

    print("Tramos de la via "+via+":")
    for i in zip(tramos, estados):
        print(i[0].decode("utf-8")+" "+i[1].decode("utf-8"))



if __name__ == '__main__':
    vias = ["MD<>VG", "MD>BC", "SE>VAL", "MD>VG", "VG>MD"]
    tramos = ["Tramo 1", "Tramo 2"]
    estados = ["Libre", "Tren 1"]

    consultarTramos("MD<>VG")

    # r.lpush('vias', *vias)
    # r.lpop('vias')
    # r.hset('MD<>VG', tramos[0], estados[0])
    # r.hset('MD<>VG', tramos[1], estados[1])

    # viasExistentes = r.lrange('vias', 0, -1)
    # hashm = r.hget('MD<>VG', tramos[1])

    # for via in viasExistentes:
    #     if("MD<>VG" == via.decode("utf-8")):
    #         print(via.decode("utf-8"))


    # print(hashm.decode("utf-8"))

    # r.set('bing3', 5)
    # print(r.get('bing3').decode("utf-8"))

    # r.incr('bing3', 5)
    # print(r.get('bing3').decode("utf-8"))