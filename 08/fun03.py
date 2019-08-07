def damage(skill01,skill02):
    damage01 = skill01 * 3
    damage02 = skill02 * 2 + 10
    return damage01,damage02

skill1_damage,skill2_damage = damage(3,6)
print(skill1_damage,skill2_damage)