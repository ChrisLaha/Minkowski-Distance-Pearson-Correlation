import math

# Data to compute
UserPRatings = {'Motorola':8, 'LG':5, 'Sony':1, 'Apple':1, 'Samsung':5, 'Nokia':7} 
UserQRatings = {'Apple':7, 'Samsung':1, 'Nokia':4, 'LG':4, 'Sony':6, 'Blackberry':3} 

# Create a class: similarity
class similarity:
    def __init__(self, ratingP, ratingQ):
        self.ratings1 = ratingP
        self.ratings2 = ratingQ
        
    # Create function to compute Minkowski, Manhattan, and Euclidean distance
    def minkowski(self, r):
        distance = 0
        for i in (set(self.ratings1.keys()) & set(self.ratings2.keys())):
            p = self.ratings1[i]
            q = self.ratings2[i]
            distance += pow(abs(p-q), r)
        return pow(distance, 1/r)
       
    # Create function to return Pearson correlation
    def pearson(self):
        sumpq = 0
        sump = 0
        sumq = 0
        sump2 = 0
        sumq2 = 0
        n = len(set(self.ratings1.keys() & set(self.ratings2.keys())))
        
        for i in (set(self.ratings1.keys()) & set(self.ratings2.keys())):
            p = self.ratings1[i]
            q = self.ratings2[i]
            sumpq += p * q
            sump += p
            sumq += q
            sump2 += pow(p,2)
            sumq2 += pow(q, 2)
            nr = (sumpq - (sump * sumq) /n)
            dr = (math.sqrt(sump2 - pow(sump, 2) /n) * math.sqrt(sumq2 - pow(sumq, 2) /n))
            r = nr/dr
        return r
    
my_class = similarity(UserPRatings, UserQRatings)
    
md = my_class.minkowski(r=1)
print(f"Manhattan Distance: ", round(md,4))

ed = my_class.minkowski(r=2)
print(f"Euclidean Distance: ", round(ed,4))

mkd = my_class.minkowski(r=3)
print(f"Minkowski Distance: ", round(mkd,4))

pc = my_class.pearson()
print(f"Pearson Correlation: ", round(pc,4))