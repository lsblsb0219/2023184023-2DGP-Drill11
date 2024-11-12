from turtledemo.sorting_animate import partition

world = [[] for _ in range(4)]
collision_pairs = {} # 빈 딕셔너리 { 'key' : [ [A list] [B list] ]

def add_collision_pair(group, a, b):
    if group not in collision_pairs:
        collision_pairs[group] = [ [], [] ] # 리스트 초기화
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)



def add_object(o, depth = 0):
    world[depth].append(o)

def add_objects(ol, depth = 0):
    world[depth] += ol


def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()


def remove_collision_object(o): # 충돌 객체 제거 함수
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)

    pass

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o) # collision pairs 에서 o를 삭제 -> 충돌 리스트에서 충돌한 거 없애기
            del o # 메모리에서 객체 자체를 삭제
            return
    raise ValueError('Cannot delete non existing object')


def clear():
    for layer in world:
        layer.clear()



# fill here
def collide(a, b):
    al,ab,ar,at = a.get_bb()
    bl,bb,br,bt = b.get_bb()

    if ar < bl: return False
    if al > br: return False
    if at < bb: return False
    if ab > bt: return False

    return True

    pass


def handle_collisions():
    # 게임월드에 등록된 충돌 정보를 바탕으로, 실제 충돌 검사를 수행.
    for group, pairs in collision_pairs.items():
        for a in pairs[0]: # A 리스트에서 하나 뽑고,
            for b in pairs[1]: # B 리스트에서 하나 뽑고,
                if collide(a, b):
                    print(f'{group} collide')
                    a.handle_collision(group, b) # 충돌한 상대가 누군지 알려줌 -> b와 충돌했어
                    b.handle_collision(group, a) # a와 충돌했어

