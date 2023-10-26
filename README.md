<!-- This readme was built off of this template: https://github.com/othneildrew/Best-README-Template/tree/master -->
<a name="readme-top"></a>


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables  
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Version][version-shield]][version-url]
[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Pull Requests][prs-shield]][prs-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="graphics/logo.png" alt="Logo" width="200" height="200">
  </a>

<h3 align="center">VerdanTech</h3>

  <p align="center">
    A garden productivity tool, agro-ecology model, and IOT platform
    for a sustainable and cooperative future.
    <br />
    <a href=""><strong>Try it yourself »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a>
    ·
    <a href="link to discord">Discord</a>
    ·
    <a href="https://youtu.be/jGFHhRVdxRM">YouTube</a>
    <br />
  </p>
</div>

VerdanTech is an open source software project best summarized as a fusion between:

1. **Garden Productivity Engine**: An intricate and interactive model of agriculture which facilitates the data-driven planning of productive spaces at any scale and the collaborative organization of labour.
- **Agro-Ecology Optimization Model**: A model which captures the relationship between agriculture and the broader ecological system, with the goal of producing a healthy abundance and diversity of food with minimal reliance on non-renewable resources and conditions of ecological destruction.
- **IoT Automation Suite**: A model which is complemented by an Internet-of-Things (IoT) platform, serving as an extensible interface for integration with external APIs. Alongside the platform is a set of embedded devices designed to automate the process of obtaining measurements and executing tasks. These devices exist in a different repository called [VerdanTech-Devices](https://github.com/nathanielarking/VerdanTech-Devices).

For a high level conceptual overview of the application's features, refer to the [Outline](outline/README.md) folder.

VerdanTech is a very young application, and most of these goals have not been completed. Refer to the [Features](#features) section for further information. VerdanTech has been in development since late 2022, or early 2021 if we count the [initial attempt](https://www.youtube.com/watch?v=w0TwPI7bLp8&ab_channel=TotalVeganicFuturism) at a similar idea. VerdanTech is built with [sentientist values](https://sentientism.info/) in mind, and as such does not consider sentient beings as acceptable subjects of exploitation for food or any other purpose.

If you wish to deploy this application yourself, see the [Deployment](#deployment) section. If the instructions are not adequate in guiding you to a successful deployment, please reach out to the [Community](#community).

The key technical features of VerdanTech are:
1. The backend is an asyncronous python HTTP and websocket application, using the [Litestar](https://litestar.dev/) ASGI framework for API, Posgresql for persisted model state, Redis for in-memory model state, a [differential synchronization](https://neil.fraser.name/writing/sync/) algorithm for multi-client synchronization, and a clean architecture with core domain logic in plain Python.
2. The frontend is a SvelteKit application configured in static adapter mode, using [Orval](https://orval.dev/) for typed client generation with [Svelte Query](https://tanstack.com/query/latest/docs/react/overview) and Tailwind + [Skeleton UI](https://www.skeleton.dev/) for UI/UX. 

<!--- See the video introduction to VerdanTech here: --->
<!--- [![Watch the video](https://img.youtube.com/vi/jGFHhRVdxRM/maxresdefault.jpg)](https://youtu.be/jGFHhRVdxRM) --->

<br />
<div>
<!-- TABLE OF CONTENTS -->
<details>
    <summary>Table of Contents</summary>
    <ul>
        <li>
            <a href="#background">Background</a>
            <ul>
                <li>
                    <a href="#the-problem">The Problem</a>
                </li>
                <li>
                    <a href="#the-solution">The Solution</a>
                </li>
            </ul>
        </li>
        <li>
            <a href="#features">Features</a>
            <ul>
                <li>
                    <a href="#completed">Completed</a>
                </li>
                <li>
                    <a href="#in-progress">In Progress</a>
                </li>
                <li>
                    <a href="#planned">Planned</a>
                </li>
            </ul>
        </li>
        <li>
            <a href="#deployment">Deployment</a>
        </li>
        <li>
            <a href="#codebase">Codebase</a>
            <ul>
                <li>
                    <a href="#built-with">Built With</a>
                </li>
                <li>
                    <a href="#architecture">Architecture</a>
                </li>
                <li>
                    <a href="#download-and-installation">Download and Installation</a>
                </li>
                <li>
                    <a href="#backend">Backend</a>
                    <ul>
                        <li>
                            <a href="#background-1">Background</a>
                        </li>
                        <li>
                            <a href="#documentation">Documentation</a>
                        </li>
                        <li>
                            <a href="#contributing">Contributing</a>
                        </li>
                    </ul>
                </li>
                <li>
                    <a href="#frontend">Frontend</a>
                    <ul>
                        <li>
                            <a href="#background-2">Background</a>
                        </li>
                        <li>
                            <a href="#documentation-1">Documentation</a>
                        </li>
                        <li>
                            <a href="#contributing-1">Contributing</a>
                        </li>
                    </ul>
                </li>
            </ul>
        </li>
        <li>
            <a href="#community">Community</a>
        </li>
    </ul>
</details>
</div>

# Background

*This section highlights the problems that VerdanTech aims to solve and the nature of the solutions.*

## What is agriculture?

Dictionary.com [defines agriculture as](https://www.dictionary.com/browse/agriculture):
> the science, art, or occupation concerned with cultivating land, raising crops, and feeding, breeding, and raising livestock; farming.

VerdanTech is built with [sentientist values](https://sentientism.info/) in mind, and as such does not consider sentient beings as acceptable subjects of exploitation for food or any other purpose. As a result, the word agriculture in the context of any VerdanTech documentation uses this definition:
> the science, art, or occupation concerned with cultivating land and raising crops; farming.

## What is ecology?

Merriam Webster [defines ecology as](https://www.merriam-webster.com/dictionary/ecology)
> a branch of science concerned with the interrelationship of organisms and their environments, the totality or pattern of relations between organisms and their environment.



Humans are organisms and are dependent on continuous exchanges of energy and materials with surrounding ecological systems, called [social metabolism]().

## What is agro-ecology?

Reliance on unsustainability means eventual collapse

## What is the Relationship Between Modern Industrial Agriculture and Ecology?

## What Adaptation is Required to Shift Our Agriculture Systems Into Ecological Sustainability?

Use less energy totsl
Usr less fossil energy
Create more biodiverse systems
Create more decentralized systems
Increased human labour

## What Are the social elements of this required adaptation?*


## *How could a technological innovation best serve to maximize the ability of humans to undertake this adaptation?*
being able to expirement systematically with various types of growing systemr

## *What is VerdanTech? How does it aim to move in this direction?*

## *What are the core values of VerdanTech as a project?*

## *What are the core values of VerdanTech as a software system?*





Agriculture is essential to our existence, and interacts with ecology. The


Agriculture is absolutely essential to our existence. Like all human activity, it s

Agriculture is a realm of production which is absolutely essential to our existence. Like all human activity, it takes place within an ecological system and interacts with that system in a way that isn't usually simple. The 
and the character of the interaction between these systems has implications for how they will tend to evolve into the future. they will set the course for our collective future..

the exchanges of energy and materials those activities product creates a pathway our systems take within the broad ecological system of the earth.

Our current mode of production is organized around fossil fuels. The extreme energy density of coal, oil, and gas is relied on to power machines and to synthesize fertilizer and pesticides.   

To communicate the intent of VerdanTech to contribute to agroecology, here is how it relates to [ten elements of agroecology (FAO)](https://www.fao.org/agroecology/overview/overview10elements/en/): 

Diversity: the reason behind the uniformity of modern industrial agriculture is that simple monoculture strategies are incredibly good at maximizing output (when paried with energy dense fuels and our modern machines) and thus, optimizing agriculture - when the objective of optimization is to produce as much product as possible. When we step into an ecological perspective - the benefit that diversity provides in terms of system resilience and sustainability also contributes to our objective. The problem that this brings is that diversity isn't easy - simple strategies require simple models, and this is true as we move more polyculture. How do we quantify diverstiy, how do we optimize for it? the inclustion of diversity into our practices means a complexification of models (relative to industrial monocropping), and how do we adapt to that? VerdanTech seeks to quantify both what diverity looks like in terms of its benefits and how it is achieved with technique, and apply that objective to real world problems so as to assist us. The better an informational model we have, the less is required of us in terms of physical precision and energy of action. Paths from a current ecosystem to one which meets the objective should be accessible to as many people as possible, even those who don't   


Co-creation and sharing of knowledge: The prospect of humans surviving ecological catastrophe through the creation of cooperative society requires the integration of knowledge across people and across the disciplines of biology, ecology, sociology, engineering. VerdanTech aims to be a platform that serves exactly the purpose of being a tool that enables cooperative human adaptation by allowing integrated models of biology and ecologoy to directly take on, add to, and share the knowledge of the human brain of agro-ecology theory and practice from those who have it and are willing to add to the probject and anyone who has access to the software and the tools.   



Synergies: The benefit of diversity is synergy, and mapping out the web of relations between all the species we have access to is a large task. VerdanTech aims to be an application which can take on this information in a digital model and be updated according to new knowledge. We can learn how to optimize biodiversity for synergy and spread that knowledge to anyone who has access to the tools.


Efficiency: Modern industrial agriculture relies on the extreme energy density and abundance of fossil fuels to maintain its productivity. A world with less or no fossil fuels implies a extreme need to produce similar amounts of food with less energy. This implies three things: less use of energy overall especially liquid fuels, more use of renewable energy, which tends to be lower in magnitude and thus we should prefer more precise and efficient use of electricityr, and more human labour than we do now. X percent of people were farmers 100 years ago, X are today. By creating an integrated-model of agro ecology we can constrain and also optimize  for the use of energy and labour, and create a horizontal basis for the collaboration of different peoples labour to maintain the same complex systems.

Recycling: nothing specific on this

Resilience: enhanced resilience of people, communities and ecosystems is key to sustainable food and agricultural systems.

Human and social value

Human and social values: protecting and improving rural livelihoods, equity and social well-being is essential for sustainable food and agricultural systems.
Culture and food traditions

Culture and food traditions: by supporting healthy, diversified and culturally appropriate diets, agroecology contributes to food security and nutrition while maintaining the health of ecosystems.
Land and natural resources governance

9 Responsible governance and 10 Circular and solidarity economy: by creating a platform that can be hosted by anyone, the organization of efforts can be made as horizontal as the users are able to be. The creation of effective modelling and producitivy tools that can be used by anyone is in the direction of puting the power of food soverignetly into more hands.  the people who consume the food, the people who create the food, and the people who control the efforts of making the food can increasingly become the same group of people. 

Circular and solidarity economy: circular and solidarity economies that reconnect producers and consumers provide innovative solutions for living within our planetary boundaries while ensuring the social foundation for inclusive and sustainable development.
Publications




Like all human activity, it takes place within an ecological system. 

The interaction between our cultivation and ecology determines what pathways we take within the model of the system.



Agriculture is an realm of human production which is absolutely essential to our existence. Like all activities, it takes place not in an isolated context but within a broad ecological system. The way we do agriculture places us in a certain pathway within the model of the system, and this model can tend towards long term sustainability or it cannot.

Our current mode of production is organized around fossil fuels as an extremely energy dense input, used both for synthesis of fertilizer and the powering of great machines to perform all the mechanical labour.

It is not organized around, but similarity dependent on ecological factors such as soil biodiversity, in a way which when out of balances contributes to the hyper problem of ecological destruction that comes back eventually as an existential threat also.

It is my belief that these conditions will end soon, and not by our own adaptation but by the conditions by which we supply the energy and the sinks ending.

These conditions ending implies a burden on humans to adapt our agriculture systems as rapidly as possible to avoid as much catastrophe and suffering as possible. This burden looks like three things:

1. Less access to dense energy sources requires a higher percentage of humans than is now, at x percent in x average countries, participating in agriculture. How do we train new people on the practice of agriculture and better allow groups of humans even with dissimiar experiences to collaborate and join their forces to building a sustainable and fruitful system? The answer to this is the productivity side of the software.

2. Due to the reliance on fossil fuels and industrial production, much knowledge on how humans can run sustainable agricutulre systems has been lost. Additionally, while the requirements for how productive these systems need to be can be drastically reduced by improvements in the social factors of the distribution and production systems, it will still remain high compared to what the average human produces now maintaining their small-scaled sustainable agriculture systems. This implies that in order for humans to adapt to new conditions with minimal suffering, we must master a whole new domain of the problem space of agricultural production within an sustainability constrained ecological environment. This will required modelling, and this is the problem solved by the ecological modelling side of the software.

3. Fuse these two ideas by creating a flexible tool that can absorb the information of human experience, through configuration and extension of the software, and digitize as much as possible of both the scientific details of the biophysical systems we want to maintain and the details of the social organization needed to maintain that system in terms of labour. 


What's the problem?

Problem is that modern agriculture is extremely unsustainable. While we produce enough food to feed the world, and world hunger is largely a result of the inefficencies or malpractice by mis-aligned social systems, the way in which we product it is not aligned with continuing production for future people.

The state of having such a small percentage of our society being involved in food production is a modern phenomona made possible by the energy density of fossil fuels. Assuming a shift to reliance on renewable power systems, a future agriculture system will be different in two key ways:

- The first is that the structure of labour that goes into how we product our food will have to change. More people will have to be involved in the process. With what technology do we most empower humans to adapt to this world?  
- The second is that the way in which we actually bio-physically grow will have to change. We can't rely on monocultures and the big machines that plow them. We'll have to spacially and genetically diversify our agriculture systems. This adds more complexity, which makes the task of more people getting involved in agriculture more difficult. 

VDT has pursues three main goals:

- Create technology that lowers the barriers toward the labour transition of future sustainable agriculture cause by a dependence on the use of energy dense fossil fuels to maintain a smaller and smaller highly specialized proffesional industry that is efficient, but brittle.
- Create a software platform for modelling what a sustainable agriculture looks like, including optimums along as many axes as possible like poly vs. monoculture, irrigation, microclimates.
- Promote to the highest extent possible the flourishing of horizontal networks cooperation to solve these problems.

There are three steps to building a system like this. The plan looks like this:
1. (The model stage) Create a dual agriculture biophysical modelling software and web application. This will try to occupy the spectrum in and between "biophysical modelling software" and "garden productivity tool." The application fulfills the following:
- Something which can be useful in any capacity, from planning the planting calendar for a single pot on your deck, to managing and optimizing entire plots with tens of thousands of plants.
- Something which seeks, as a driving force, the off-loading of informational complexity requirements away from humans and onto software systems, and the immortalization of vital human knowledge into algorithms and databases. The purpose of these things is not to take these things away from humans but to enable the sharing of this knowledge between humans through smart tools that enable people to learn and reflect the knowledge within and not just producing the right outputs.
- The tool must have a high degree of co-operation-ability, as in the modelling systems should be made to work like google docs over notepad, it should be as seamless as possible to collaborate in real time with others in the process of using the model.
- The software must be as maintainable, extensible, and transparent as possible. The slope of the graph of complexity over time should be as flat as possible due to high cohesion and minimal coupling in the software.
- The software must be performant and make use of the best available technologies to as to minimize technical debt (why I chose Litestar and Svelte)
- The software must be open-source and if it is to succeed, foster a community around it with shared values and a horizontal structure of labour and cooperation to make the software better over time.
- The software should depend on other software as much as possible with values that is aligned with it, such as Litestar which is a community driven project.
2. (The input stage) While the software model exists, it still relies primary on humans to gather the information to sustain it, and update the model state. Technologies must be made to automate the process of acquiring information. In the model level, the model will have an interface for plugging in external information and control devices. The simplest are weather APIs, and then there's physical sensors in the garden space, and finally there are quadcopters with cameras conducting daily complete 3D scans of the area and computer vision systems categorizing that information into inputs into the model. The end game of this is that the entire informational side of agriculture is automated, and the barrier to entry with a system like this to growing your own food is setting up the model and the input-gatherers and then performing the physical "actions" which are outputs of the model to optimize state.  
3. (The output stage) Complete automation can be achieved at such a time as there are robotic systems capable of carrying out the vast complexity of operations humans perfore in agriculture. This is still totally sci-fi, but there are companies working on it today for specialized tasks.

Input devices include temperature, moisture, rain, wind, and soil sensors, as well as autonomous camera drones capable of determining system state through computer vision. Output devices include irrigation controllers and general purpose robotic cultivators. 

<p align="right"><a href="#readme-top">back to top</a></p>

# Features

The (Outline)[outline/overview.md] folder contains conceptual design documents and is used to continuously plan and document the application at a high level. Refer to it for user interface wireframes and domain models. This section summarizes the completion state of the features.

## Completed

## In progress

- User Management
    - [x] User datastructure as a container for human users of the application.
    - [] User CRUD.
    - [x] Email verification.
    - [x] Password reset.
    - [] Authentication.

## Planned

- User Management
    - [] Authentication.

- Garden Management
    - [ ] Garden datastructure as a top-level container for an environment and GardenMembership as a link between User and Gardens.
    - [ ] Garden CRUD.
    - [ ] Garden membership management, including invitation, acceptance, rejection, revoke.
    - [ ] Garden membership permissions management, including admin, edit, and view roles.

- Workspace Container
    - [ ] Workspace datastructure as a container for a localized space. PlantingArea datastructure as a container representing space that can be used for cultivation.
    - [ ] Workspace and PlantingArea CRUD.

- Cultivar Records
    - [ ] Cultivar as a datastructure for the attributes of plant variations. CultivarSet as a datastructure for grouping Cultivars.
    - [ ] Cultivar and CultivarSet CRUD.
    - [ ] Cultivar parent-chield Variety system.
    - [ ] CultivarSets merging, switching.
    - [ ] WestCoastSeeds CultivarSet.

- Plant Instancing

- Differential Synchronization

- Bulk Update Tools

- Planting Schema Generation

- Actions Outputs

- Device Management


# Deployment

There are two ways (planning) to deploy: manual mode on linux and docker mode. Even if you don't know docker I recommend it more cause its easy with docker desktop. More likely you want to run this on a raspbery pi and it's easy there two. But idk how you would manually install tihs on non-linux


# Codebase

## Built With

* [![Svelte][Svelte.dev]][Svelte-url]

## Architecture

The application implements a decoupled backend/frontent arhitecture. The backend is an asynchronous python3. running on uvicore, and the frontend is a SvelteKit spa-mode static file generator with Skeleton UI.

## Download and Installation

Recommended VS code theme: Solarized Dark

## Backend

### Background

The python backend implements a clean architecture pattern, meaning that the functions of the application are segregated in a way that minimizes coupling. Quick summaries for the layers:
- The domain layer holds the core business logic and is made up of four components: Entities, which are objects with IDs and individuality that represent concepts in the problem space, RootEntities which are entities that make up Collections of documents or SQL tables in the database, meaning they represent consistency boundaries of data, value objects, which are ID-less and immutable, and represent individual-less states, and services, which encapsulate core logic in the problem domain that can't be relegated to any of the other options. All these concepts are implemented using native Python dataclasses. The domain layer also holds interfaces that are relied upon by the domain layer and application layer
- The application layer orchestrates the domain layer and connects it to implementations of the interfaces. The application layer has two parts: the operaions sections, which are high level application functions and make up the main API (are-one to one with http API routes), and the services sections, which comprise more granular orchestrations of the domain logic and are called in the operations.
- The infrastrure contains implementations of the domain service interfaces, such as database implementations of the repository interface. The only repository in use so far is a MongoDB Motor (async pymongo) implementation. The repository abstraction makes it possible to use different implementations in the future, but I havent investigated the potential compatibility with a sql database (plan to stick with mongo)
- The API layer is the http and websocket wrapping around the application layer, and is implemented using the Litestar 

### Documentation

### Contributing

## Frontend

### Background

Why I chose Svelte and Skeleton.

### Documentation

### Contributing

# Community



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

<!-- IN-REPO -->
[version-shield]: https://img.shields.io/badge/version-0.0.1-blue?style=for-the-badge
[version-url]: https://github.com/nathanielarking/Autonomous-Agriculture/releases
[contributors-shield]: https://img.shields.io/github/contributors/nathanielarking/VerdanTech.svg?style=for-the-badge
[contributors-url]: https://github.com/nathanielarking/VerdanTech/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/nathanielarking/VerdanTech.svg?style=for-the-badge
[stars-url]: https://github.com/nathanielarking/VerdanTech/stargazers
[issues-shield]: https://img.shields.io/github/issues/nathanielarking/VerdanTech.svg?style=for-the-badge
[issues-url]: https://github.com/nathanielarking/VerdanTech/issues
[prs-shield]: https://img.shields.io/github/issues-pr/nathanielarking/VerdanTech.svg?style=for-the-badge
[prs-url]: https://github.com/nathanielarking/VerdanTech/pulls
[license-shield]: https://img.shields.io/github/license/nathanielarking/VerdanTech.svg?style=for-the-badge
[license-url]: https://github.com/nathanielarking/VerdanTech/LICENSE.txt

<!-- OTHER-REPO -->
[devices]: https://github.com/nathanielarking/VerdanTech-Devices

<!-- EXTERNAL -->

[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
