# 构建maven自定义archetype

```
mvn archetype:create-from-project
cd target
mvn clean install
mvn archetype:crawl
mvn archetype:generate -DarchetypeCatalog=local
cp \repository\org\apache\maven\archetypes\scaffold-archetype
mvn archetype:generate -DgroupId=org.example.monolith -DartifactId=monolith -DarchetypeArtifactId=scaffold-archetype -DarchetypeVersion=1.0-SNAPSHOT -DinteractiveMode=false
```