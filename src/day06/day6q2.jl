using Printf
numberOfDays = 256

fishList = open("/Users/mjpmorse/AdventofCode2021/data/data_q6_dummy.txt","r") do datafile
    [parse.(Int64, split(line, ',')) for line in eachline(datafile)]
end
fishList = fishList[1]


# println(fishList)

for day in 1:numberOfDays
    global fishList
    fishList = fishList .- 1
    numberNewFish = length(fishList[fishList.==-1])
    
    for fish in 1:numberNewFish
        global fishList
        fishList = append!(fishList, 8)
    end
        
    fishList[fishList.==-1] .= 6
    # println(fishList)  
end

numberOfFish = length(fishList)

@printf "The number of fish after %i days is %i \n" numberOfDays numberOfFish