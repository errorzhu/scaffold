# 构建maven自定义archetype

```
mvn archetype:create-from-project
mvn archetype:crawl
mvn archetype:generate -DarchetypeCatalog=local
mvn archetype:generate -DgroupId=org.example.monolith -DartifactId=monolith -DarchetypeArtifactId=scaffold-archetype -DarchetypeVersion=1.0-SNAPSHOT -DinteractiveMode=false
```