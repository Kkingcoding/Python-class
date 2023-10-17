treeHit = 0

while treeHit < 10:
    treeHit += 1
    print("You hit the tree %d times." % treeHit)
    if treeHit == 10:
        print("The tree is falling.")

        
while treeHit < 10:
    treeHit += 1
    if treeHit % 2 == 0:
        continue #while문 처음으로 돌아감
    print(f"You hit the tree {treeHit} times.")
    if treeHit == 10:
        print("The tree is falling.")
        #continue
