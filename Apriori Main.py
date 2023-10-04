import time

start_time = time.time()

class pattern:
    def __init__(self,iset,s):
        self.itemset = iset.copy()
        self.support = set()
       
       
       
       
c = []
c.append([])
L = []
L.append([])
itemset = []
path = "C:\\Users\\USER\\Desktop\\apriori\\connect.dat"




def frequent_subsets(itemset, min_support):
    frequent_itemsets = []
    for item in itemset:
        # Calculate the support count for each itemset.
        support_count = 0
        with open(path, "r") as fptr:
            for line in fptr:
                token = line.split()
                if set(item.itemset).issubset(token):
                    support_count += 1

        # Check if the itemset's support meets the minimum support threshold.
        if support_count >= min_support:
            item.support = support_count
            L[0].append(item)
            frequent_itemsets.append(item)
    return frequent_itemsets












def join(frequent_itemsets):
    demo_candidate_itemsets = []
    k = len(frequent_itemsets[0].itemset)  

    for i in range(len(frequent_itemsets)):
        for j in range(i + 1, len(frequent_itemsets)):
            # first (k-1) items from each itemset
            first_items_i = list(frequent_itemsets[i].itemset)[:k - 1]
            first_items_j = list(frequent_itemsets[j].itemset)[:k - 1]

            if first_items_i == first_items_j:
               # set is used to use union oooperation.
                candidate_items = set(frequent_itemsets[i].itemset).union(frequent_itemsets[j].itemset)
                candidate = pattern(candidate_items, 1)
                demo_candidate_itemsets.append(candidate)

    return demo_candidate_itemsets







def downard_closure_property(candidate_itemsets, frequent_itemsets):
    
    final_candidates = []
    
    subsets = [candidate_itemsets - {item} for item in candidate_itemsets]
    for subset in subsets:
        if subset in frequent_itemsets:
            final_candidates.append(subset)
    
    return final_candidates






fptr = open(path,"r")
n= 0
while True:
    line = fptr.readline()
   
    if not line:
        break
    n+=1
   
   # print(line)
   
    token = line.split()
   # print(token)
    token.sort()
    #print(token)
    p = []
    for i in token:
        p.append(i)
        temp = pattern(p,1)
        p.clear()
        flag = False
        if temp.itemset not in [item.itemset for item in itemset]:
            temp.path = path
            itemset.append(temp)

fptr.close()
min_support = 65000

frequent_itemset = frequent_subsets(itemset, min_support)
#candidate_itemset = downard_closure_property(itemset, frequent_itemset)
#k = 1

print("C1:")
for item in itemset:
   print("{" + ', '.join(map(str, item.itemset)) + "} : " + str(item.support))
print()

print("L1:")
for item in frequent_itemset:  #join only works for string thats why conversion
    print("{" + ', '.join(map(str, item.itemset)) + "} : " + str(item.support))
print()



k = 1   #num of iteration

counts = {}
counts['Length-1 Frequent Patterns'] = len(L[0])

while L[k - 1]:
    k += 1
    c.append([])
    L.append([])
    c[k - 1] = join(L[k - 2])

    frequent_itemsets = frequent_subsets(c[k - 1], min_support)
    L[k - 1].extend(frequent_itemsets)
    counts[f'Length-{k} Frequent Patterns'] = len(L[k-1])

    print(f"C{k}:")
    for item in c[k - 1]:
        print("{" + ', '.join(map(str, item.itemset)) + "} : " + str(item.support))
    print()

    print(f"L{k}:")
    for item in frequent_itemsets:
        print("{" + ', '.join(map(str, item.itemset)) + "} : " + str(item.support))
    print()
    
for key, value in counts.items():
    print(f"Total number of {key}: {value}")
#main(pattern(iset, s))
end_time = time.time()
runtime = end_time - start_time

print("Code runtime: {:.6f} seconds".format(runtime))