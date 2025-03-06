def sysCall_init():
    sim = require('sim')
    bot_body = sim.getObjectHandle('bot_body')
    right_joint = sim.getObjectHandle('right_joint')
    left_joint = sim.getObjectHandle('left_joint')
    g = 9.8
    l= 0.01
    m= 0.05
    A = [ 0, 1;
          g/l , 0; ]
    B= [0;
        1/(m*l*l)]
    Q = [1,0,;
         0,1;]
    R = 1;    
    
def sysCall_actuation():
    local state = sim.getScriptSimulationParameter(sim.handle_self, 'state')
    local position = sim.getObjectPosition(bot_body, -1)
    local orientation = sim.getObjectOrientation(bot_body, -1)
    local velocity = sim.getObjectVelocity(bot_body)
    local angularVelocity = sim.getObjectAngularVelocity(bot_body)
   
    [K,S,P] = lqr(A,B,Q,R,N)
    local state = {x1, x2, x3, x4}
    local control_signal = -self.K[1]*state[1] - self.K[2]*state[2] - self.K[3]*state[3] - self.K[4]*state[4]
    sim.setJointTargetVelocity(self.right_joint, control_signal)
    sim.setJointTargetVelocity(self.left_joint, control_signal)
    pass

def sysCall_sensing():
    
    local position = sim.getObjectPosition(bot_body, -1)
    local orientation = sim.getObjectOrientation(bot_body, -1)
    local velocity = sim.getObjectVelocity(bot_body)
    local angularVelocity = sim.getObjectAngularVelocity(bot_body)
    local desired_position = 0
    local desired_velocity = 0
    local desired_angle = 3.14
    local desired_angular_velocity = 0
    
     x1 = position[1] -desired_position
     x2 = velocity[1] - desired_velocity
     x3 = orientation[2] -desired_angle
     x4 = angularVelocity[2] - desired_angular_velocity
     local state = {x1, x2, x3, x4}
    sim.setScriptSimulationParameter(sim.handle_self, 'state', state)
    pass

    def sysCall_cleanup():

    local bot_body = sim.getObjectHandle('bot_body')
    local right_joint = sim.getObjectHandle('right_joint')
    local left_joint = sim.getObjectHandle('left_joint')

    
    sim.setObjectPosition(bot_body, -1, {0, 0, 0})
    sim.setObjectOrientation(bot_body, -1, {0, 0, 0})

    
    sim.setJointTargetVelocity(right_joint, 0)
    sim.setJointTargetVelocity(left_joint, 0)

    pass