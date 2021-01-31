FROM baseimagesrepo/azurite
FROM baseimage:reuse AS Reuse
FROM baseImage:args AS args
FROM baseImage/linux:tag AS tags
FROM baseImage:minecraftutils AS mc 
FROM baseImage:pile AS user 
FROM imageUser:function AS user1
FROM platformUser:function AS utility
FROM minecraftutils:mc AS minecraft 
FROM platformCUDA:cuda AS functionCUDA
FROM CUDA:function AS var1 
FROM basePlatform:function:tag AS cudaUtilityManager 
FROM functionCUDA:tag:args_baseImageForm AS CUDAt_1
#Lots of docker ahead. So many cuda loadings. 
FROM platformCUDA:cuda AS functionCUDA1
FROM platformCUDA:cuda AS functionCUDA2
FROM platformCUDA:cuda AS functionCUDA3
FROM platformCUDA:cuda AS functionCUDA4
FROM platformCUDA:cuda AS functionCUDA5
FROM platformCUDA:cuda AS functionCUDA6
FROM platformCUDA:cuda AS functionCUDA7
FROM platformCUDA:cuda AS functionCUDA8
FROM platformCUDA:cuda AS functionCUDA9
FROM platformCUDA:cuda AS functionCUDA10
FROM platformCUDA:cuda AS functionCUDA11
FROM platformCUDA:cuda AS functionCUDA12
FROM platformCUDA:cuda AS functionCUDA13
FROM platformCUDA:cuda AS functionCUDA14
FROM platformCUDA:cuda AS functionCUDA15
FROM platformCUDA:cuda AS functionCUDA16
FROM platformCUDA:cuda AS functionCUDA17
FROM platformCUDA:cuda AS functionCUDA18
FROM platformCUDA:cuda AS functionCUDA19
FROM platformCUDA:cuda AS functionCUDA20
#load minecraftutils
FROM minecraftutils:mc AS minecraft1
FROM minecraftutils:mc AS minecraft2
FROM minecraftutils:mc AS minecraft3
FROM minecraftutils:mc AS minecraft4
FROM minecraftutils:mc AS minecraft5
FROM minecraftutils:mc AS minecraft6
FROM minecraftutils:mc AS minecraft7
FROM minecraftutils:mc AS minecraft8
FROM minecraftutils:mc AS minecraft9
FROM minecraftutils:mc AS minecraft10
#load core services
FROM coreBase:tags AS tags2 
