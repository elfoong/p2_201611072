﻿def schoolSatisfy():
    alldata=list()
    alldata=[
    ["Division","Very satisfied","Satisfied","Unsatisfied","Very unsatisfied"],
    ["Class quality",13.1,37.1,8.7,1.5],
    ["Class way",10.6,34.6,13.4,1.9],
    ["Friendship",27.1,40.0,2.9,1.5],
    ["Relationship with teacher",16.2,37.8,6.8,0.8],
    ["Facility",11.4,29.8,14.8,4.9],
    ["Environment around schools",12.2,26.5,14.9,4.4],
    ["Major",13.5,29.7,11.1,2.4],
    ["School life",13.7,37.6,4.1,1.2]
    ]
    data=alldata[1:]
    sasum=0
    unsum=0
    for i in data:
        sum=i[1]+i[2]
        sasum+=sum
        sum=i[3]+i[4]
        unsum+=sum
    saaver=sasum/len(data)
    unaver=unsum/len(data)
    print "Satisfied average is %s"%saaver
    print "Unsatisfied average is %s"%unaver

def presidentWords():    
    washionton=list()
    washington=[
    "Fellow Citizens:"
    "I AM again called upon by the voice of my country to execute the functions of its Chief Magistrate. When the occasion proper for it shall arrive, I shall endeavor to express the high sense I entertain of this distinguished honor, and of the confidence which has been reposed in me by the people of united America."
    "Previous to the execution of any official act of the President the Constitution requires an oath of office. This oath I am now about to take, and in your presence: That if it shall be found during my administration of the Government I have in any instance violated willingly or knowingly the injunctions thereof, I may (besides incurring constitutional punishment) be subject to the upbraidings of all who are now witnesses of the present solemn ceremony."
    ]
    
    bush=list()
    bush=[
    "President Clinton, distinguished guests and my fellow citizens, the peaceful transfer of authority is rare in history, yet common in our country. With a simple oath, we affirm old traditions and make new beginnings."
    "As I begin, I thank President Clinton for his service to our nation."
    "And I thank Vice President Gore for a contest conducted with spirit and ended with grace."
    "I am honored and humbled to stand here, where so many of America's leaders have come before me, and so many will follow."   
    "We have a place, all of us, in a long story - a story we continue, but whose end we will not see. It is the story of a new world that became a friend and liberator of the old, a story of a slave-holding society that became a servant of freedom, the story of a power that went into the world to protect but not possess, to defend but not to conquer."
    "It is the American story - a story of flawed and fallible people, united across the generations by grand and enduring ideals."
    "The grandest of these ideals is an unfolding American promise that everyone belongs, that everyone deserves a chance, that no insignificant person was ever born."
    "Americans are called to enact this promise in our lives and in our laws. And though our nation has sometimes halted, and sometimes delayed, we must follow no other course."
    "Through much of the last century, America's faith in freedom and democracy was a rock in a raging sea. Now it is a seed upon the wind, taking root in many nations."
    "Our democratic faith is more than the creed of our country, it is the inborn hope of our humanity, an ideal we carry but do not own, a trust we bear and pass along. And even after nearly 225 years, we have a long way yet to travel."
    "While many of our citizens prosper, others doubt the promise, even the justice, of our own country. The ambitions of some Americans are limited by failing schools and hidden prejudice and the circumstances of their birth. And sometimes our differences run so deep, it seems we share a continent, but not a country."
    "We do not accept this, and we will not allow it. Our unity, our union, is the serious work of leaders and citizens in every generation. And this is my solemn pledge: I will work to build a single nation of justice and opportunity."
    "I know this is in our reach because we are guided by a power larger than ourselves who creates us equal in His image."
    "And we are confident in principles that unite and lead us onward."
    "America has never been united by blood or birth or soil. We are bound by ideals that move us beyond our backgrounds, lift us above our interests and teach us what it means to be citizens. Every child must be taught these principles. Every citizen must uphold them. And every immigrant, by embracing these ideals, makes our country more, not less, American."
    "Today, we affirm a new commitment to live out our nation's promise through civility, courage, compassion and character."
    "America, at its best, matches a commitment to principle with a concern for civility. A civil society demands from each of us good will and respect, fair dealing and forgiveness."
    "Some seem to believe that our politics can afford to be petty because, in a time of peace, the stakes of our debates appear small."
    "But the stakes for America are never small. If our country does not lead the cause of freedom, it will not be led. If we do not turn the hearts of children toward knowledge and character, we will lose their gifts and undermine their idealism. If we permit our economy to drift and decline, the vulnerable will suffer most."
    "We must live up to the calling we share. Civility is not a tactic or a sentiment. It is the determined choice of trust over cynicism, of community over chaos. And this commitment, if we keep it, is a way to shared accomplishment."
    "America, at its best, is also courageous."
    "Our national courage has been clear in times of depression and war, when defending common dangers defined our common good. Now we must choose if the example of our fathers and mothers will inspire us or condemn us. We must show courage in a time of blessing by confronting problems instead of passing them on to future generations."
    "Together, we will reclaim America's schools, before ignorance and apathy claim more young lives."
    "We will reform Social Security and Medicare, sparing our children from struggles we have the power to prevent. And we will reduce taxes, to recover the momentum of our economy and reward the effort and enterprise of working Americans."
    "We will build our defenses beyond challenge, lest weakness invite challenge."
    "We will confront weapons of mass destruction, so that a new century is spared new horrors."
    "The enemies of liberty and our country should make no mistake: America remains engaged in the world by history and by choice, shaping a balance of power that favors freedom. We will defend our allies and our interests. We will show purpose without arrogance. We will meet aggression and bad faith with resolve and strength. And to all nations, we will speak for the values that gave our nation birth."
    "America, at its best, is compassionate. In the quiet of American conscience, we know that deep, persistent poverty is unworthy of our nation's promise."
    "And whatever our views of its cause, we can agree that children at risk are not at fault. Abandonment and abuse are not acts of God, they are failures of love."
    "And the proliferation of prisons, however necessary, is no substitute for hope and order in our souls."
    "Where there is suffering, there is duty. Americans in need are not strangers, they are citizens, not problems, but priorities. And all of us are diminished when any are hopeless."
    "Government has great responsibilities for public safety and public health, for civil rights and common schools. Yet compassion is the work of a nation, not just a government."
    "And some needs and hurts are so deep they will only respond to a mentor's touch or a pastor's prayer. Church and charity, synagogue and mosque lend our communities their humanity, and they will have an honored place in our plans and in our laws."
    "Many in our country do not know the pain of poverty, but we can listen to those who do."
    "And I can pledge our nation to a goal: When we see that wounded traveler on the road to Jericho, we will not pass to the other side.    America, at its best, is a place where personal responsibility is valued and expected."
    "Encouraging responsibility is not a search for scapegoats, it is a call to conscience. And though it requires sacrifice, it brings a deeper fulfillment. We find the fullness of life not only in options, but in commitments."
    "And we find that children and community are the commitments that set us free."
    "Our public interest depends on private character, on civic duty and family bonds and basic fairness, on uncounted, unhonored acts of decency which give direction to our freedom."
    "Sometimes in life we are called to do great things. But as a saint of our times has said, every day we are called to do small things with great love. The most important tasks of a democracy are done by everyone."
    "I will live and lead by these principles: to advance my convictions with civility, to pursue the public interest with courage, to speak for greater justice and compassion, to call for responsibility and try to live it as well."
    "In all these ways, I will bring the values of our history to the care of our times."
    "What you do is as important as anything government does. I ask you to seek a common good beyond your comfort; to defend needed reforms against easy attacks; to serve your nation, beginning with your neighbor. I ask you to be citizens: citizens, not spectators; citizens, not subjects; responsible citizens, building communities of service and a nation of character."
    "Americans are generous and strong and decent, not because we believe in ourselves, but because we hold beliefs beyond ourselves. When this spirit of citizenship is missing, no government program can replace it. When this spirit is present, no wrong can stand against it."
    "After the Declaration of Independence was signed, Virginia statesman John Page wrote to Thomas Jefferson: “We know the race is not to the swift nor the battle to the strong. Do you not think an angel rides in the whirlwind and directs this storm?”"
    "Much time has passed since Jefferson arrived for his inauguration. The years and changes accumulate. But the themes of this day he would know: our nation's grand story of courage and its simple dream of dignity."
    "We are not this story's author, who fills time and eternity with his purpose. Yet his purpose is achieved in our duty, and our duty is fulfilled in service to one another."
    "Never tiring, never yielding, never finishing, we renew that purpose today, to make our country more just and generous, to affirm the dignity of our lives and every life."
    "This work continues. This story goes on. And an angel still rides in the whirlwind and directs this storm."
    "God bless you all, and God bless America."
    ]
    
    was=dict()
    for sentence in washington:
        words=sentence.split()
        for word in words:
            if word in was:
                was[word]+=1
            else:
                was[word]=1
    print "Washington said"
    frewas=list()
    for i in was:
        if was[i]>=3:
            frewas.append(i)
            print "%s : %d"%(i,was[i])
    print "Washington's frequent words are",frewas
    print "------------------------------------------------------"
    bus=dict()
    for sentence in bush:
        words=sentence.split()
        for word in words:
            if word in bus:
                bus[word]+=1
            else:
                bus[word]=1
    print "Bush said"
    frebus=list()
    for i in bus:
        if bus[i]>=30:
            frebus.append(i)
            print "%s : %d"%(i,bus[i])
    print "Bush's frequent words are",frebus

def lab11():
    schoolSatisfy()
    presidentWords()

def main():
    lab11()
    
if __name__=="__main__":
    main()