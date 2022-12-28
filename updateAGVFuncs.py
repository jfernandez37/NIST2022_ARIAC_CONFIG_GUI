
def updateAgvQudrants(agvSelection, quadrantMenu, currentQuadrant, agv1Quadrants,agv2Quadrants,agv3Quadrants,agv4Quadrants, window):
    menu=quadrantMenu['menu']
    menu.delete(0,'end')
    if agvSelection.get()=='agv1':
        agv1Quadrants.remove(currentQuadrant.get())
        currentQuadrant.set(agv1Quadrants[0])
        for quadrant in agv1Quadrants:
            menu.add_command(label=quadrant, command=lambda quadrant=quadrant: currentQuadrant.set(quadrant))
    elif agvSelection.get()=='agv2':
        agv2Quadrants.remove(currentQuadrant.get())
        currentQuadrant.set(agv2Quadrants[0])
        for quadrant in agv2Quadrants:
            menu.add_command(label=quadrant, command=lambda quadrant=quadrant: currentQuadrant.set(quadrant))
    elif agvSelection.get()=='agv3':
        agv3Quadrants.remove(currentQuadrant.get())
        currentQuadrant.set(agv3Quadrants[0])
        for quadrant in agv3Quadrants:
            menu.add_command(label=quadrant, command=lambda quadrant=quadrant: currentQuadrant.set(quadrant))
    else:
        agv4Quadrants.remove(currentQuadrant.get())
        currentQuadrant.set(agv4Quadrants[0])
        for quadrant in agv4Quadrants:
            menu.add_command(label=quadrant, command=lambda quadrant=quadrant: currentQuadrant.set(quadrant))
    window.destroy()

def updateTrayIds(agv1Val, agv2Val, agv3Val, agv4Val, agv1Menu, agv2Menu, agv3Menu, agv4Menu,agvTrayIds,a,b,c):
    menu1=agv1Menu['menu']
    menu1.delete(0, 'end')
    menu2=agv2Menu['menu']
    menu2.delete(0, 'end')
    menu3=agv3Menu['menu']
    menu3.delete(0, 'end')
    menu4=agv4Menu['menu']
    menu4.delete(0, 'end')
    for id in agvTrayIds:
        if (id!=agv2Val.get() and id!=agv3Val.get() and id!=agv4Val.get()) or id=="":
            menu1.add_command(label=id, command=lambda id=id: agv1Val.set(id))
        if (id!=agv1Val.get() and id!=agv3Val.get() and id!=agv4Val.get()) or id=="":
            menu2.add_command(label=id, command=lambda id=id: agv2Val.set(id))
        if (id!=agv2Val.get() and id!=agv1Val.get() and id!=agv4Val.get())or id=="":
            menu3.add_command(label=id, command=lambda id=id: agv3Val.set(id))
        if (id!=agv2Val.get() and id!=agv3Val.get() and id!=agv1Val.get())or id=="":
            menu4.add_command(label=id, command=lambda id=id: agv4Val.set(id))
