graph = {
 'A' : ['B','C'],
 'B' : ['D', 'E'],
 'C' : ['F', 'G'],
 'D' : [],
 'E' : [],
 'F' : [],
 'G' : []
}
def DLS(start,goal,path,level,maxD):
    print('Current Level-->',level)
    path.append(start)
    if start == goal:
        print("Goal Node Found")
        return path
    print('Goal Node Not Found at thie level:',level)
    if level==maxD:
        return False
    print('Expanding The Current Node ',start, ' At this Level ',level)
    for child in graph[start]:
        if DLS(child,goal,path,level+1,maxD):
            return path
        path.pop()
    return False
start = 'A'
goal = input('Enter the goal node:-')
maxD = int(input("Enter the maximum depth limit:-"))
print()
path = list()
res = DLS(start,goal,path,0,maxD)
if(res):
    print("Path to goal node available")
    print("Path",path)
else:
    print("No path available for the goal node in given depth limit")