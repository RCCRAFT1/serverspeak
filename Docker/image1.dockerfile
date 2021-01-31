#playground.docker is used in this docker image.
FROM baseImage:tags
FROM baseImage:minecraftutils
FROM imagePlatform:playground 
FROM playground:tags 
FROM playground:tags2
#FROM playground:minecraftutils
FROM playground/hello-docker:tags 
FROM minecraftutils:mc 
FROM python:pytorch AS torch 
FROM python:cache 
FROM baseUser:default AS user 
FROM pillowMessage:jwolt AS playground
FROM basePlatformMessger:taco AS playground.tags 
FROM playground:tagManager
FROM image:playground AS tags.playground.uiBase 
FROM playground/docker-userManager AS playground.userManager 
FROM playground/docker-manager AS docker.tags 
FROM platform AS playground.platform32
