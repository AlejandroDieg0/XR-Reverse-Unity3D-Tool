This tool provides the semiautomatic generation of App documentation for Unity3D projects

# Lab Recruits Project Analysis

In this documentation we analyzed your project and its scenes "TestScene" , "Menu" and "Main".

## Guide on how to read your project documentation
In the documentation provided you have many different views and utilities to make your project more readable for someone that is approaching for the first time at it, to make software maintenance and code analysis.

In [Project Settings](project/tree.md) you can have general informations about your project, like details on deployment devices or general settings of your project.
Of them you can also view an [XML Description](project/xml.md), use these information for your own analysis.

For every scene of your project you have a section in which you have many different views of the scene compositional structure.
For example, you have in [Scene #0 "1-Menu"](scene0/scene1.md) a brief overview of your scene.
In [GameObjects View](scene0/go1.md) you can see all of the GameObjects that compose your scene in a Dot Tree view.

If you need, you also have three more views of your scene GameObjects: in [Graphs](scene0/graphs_go1.md) there are Radial, Constellation and Snowflake views of them.
You can also take a look of your scene from a MonoBehavioural point of view in [MonoBehavioural View](scene0/mb1.md), also in different kind of [Graphs](scene0/graphs_mb1.md).
If you want to know more details of the Objects in your scene, you can navigate a [Tree](scene0/tree1.md), in which are shown details of every Object linked in a scene.

When you find a GameObject in the scene of your interest, you can get informations on details of your GameObject just navigating the tree and looking for the ID of the GameObject.
In this way you can get informations about specific details (as position in scene, monobehaviour associated, name, other attributes) of the Object you're studying.
If you want to know what Script is associated at a specific MonoBehaviour, you can put in the searchbar the GUID of the script and the system will provide you the name of the related script.
To read the script listing, you just have to search the script name you find with the bar.
You can do the same also with other kind of assets.
All of these "linking" informations are provided in:

- [Scripts Meta](project/meta/metafiles_scripts.md)
- [Full Assets Meta](project/meta/metafiles_assets.md)
- [Prefab Meta](project/meta/metafiles_prefab.md)

It's also available an [XML Description](scene0/xml1.md) and a [YAML](scene0/yaml1.md) you can use by yourself to freely parse in objects serialized datas from your scene by your need.

We found many scripts linked at objects of your scenes.
You can easy navigate among them, as you have:
- [Lab](project/scripts/lab_scripts.md)
- [Character](project/scripts/character_scripts.md)
- [Connection](project/scripts/connection_scripts.md)
- [Tests](project/scripts/tests_scripts.md)
- [UI](project/scripts/ui_scripts.md)
- [Utilities](project/scripts/utilities_scripts.md)
- [World](project/scripts/world_scripts.md)

After reading your this project , I'll be grateful for compiling a little [Survey](https://docs.google.com/forms/d/1GxNW6fxVvkXlDuv-jWntsQo6O3sf1AGrQN_21Od6_nA/prefill) concerning your ideas and feedbacks on this project startup, hoping to be useful for you.
