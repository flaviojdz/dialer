import pandas as pd

def sort_agents(df_groups,df_agents):
    #initialize variables
    groups = df_groups.values.tolist()
    agents = df_agents.values.tolist()
    sorted_agents = []
    # loop for all froups
    for i in range(len(groups)):
            # append empty list to add agents
            agent_count = 0
            while agent_count < groups[i][1]:
            # check if empty for assigning agents ( not remaining agents)
            if not agents:
                break
            # check if the remaining agents doesnt have remaining hours to be assign.
            elif float(agents[0][1]) <= 0:
                agents.pop(0)
                break
            # remove the agent from list to evalute its involvement
            temp_agent = agents.pop(0)
            # reduce the group to check status
            needed_group = groups[i][1] - agent_count

            # check if we have more workinmg hours than needed for the group
            if float(temp_agent[1]) > needed_group:
                not_assigned_agent = temp_agent.copy()
                not_assigned_agent[1] = float(not_assigned_agent[1]) - needed_group
                # append at the beginning:
                agents.insert(0, not_assigned_agent)
                # calculate assigned to list
                temp_agent[1] = float(temp_agent[1]) - float(not_assigned_agent[1])
            # add agent to new list
            temp_agent[2] = groups[i][0]
            sorted_agents.append(temp_agent)
            agent_count += float(sorted_agents[-1][-2])
    #adding mix agents
    if agents:
        for i in range(len(agents)):
            temp_agent = agents.pop(0)
            temp_agent[2] = 'MIXED_AGENTS'
            sorted_agents.append(temp_agent)
    # redefine columns if we are not quering cloudtalk_campaign_id
    df = pd.DataFrame(columns=df_agents.columns.values)
    df = df.append(pd.DataFrame(sorted_agents, columns=df_agents.columns.values))
    return df
