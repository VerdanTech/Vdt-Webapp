# VerdanTech - The Collaborative Garden Productivity Tool

Logo

VerdanTech is an open source software application best described as a fusion between:

1. **Garden productivity**: A model of the problem space of agriculture which allows us to manipulate it in a way which produces information that is useful to the horizontal organization of our physical labour. 
- **Agro-ecology modelling**: A model of the relationship between agriculture and the broader ecological system which allows us optimize the objective of producing a healthy abundance and diversity of food for all people while minimizing the unsustainable condition of our reliance on both large quantities of non-renewable resources and the destruction of the ecological context of the Earth system.  
- **Internet-of-things automation suite**: A suite of embedded devices aimed at automating the process of both the collection of input data which describes the state of the system and the enactment of the physical outputs required for optimization. Input devices include temperature, moisture, rain, wind, and soil sensors, as well as autonomous camera drones capable of determining system state through computer vision. Output devices include irrigation controllers and general purpose robotic cultivators. These devices live in a different repository called (VerdanTech-Devices)[https://github.com/nathanielarking/VerdanTech-Devices].

VerdanTech is a very immature application, and most of these goals have not been completed. See (Roadmap)[## Roadmap] for further information. VerdanTech has been in development since late 2022, or early 2021 if you count the (first attempt)[https://www.youtube.com/watch?v=w0TwPI7bLp8&ab_channel=TotalVeganicFuturism] at a similar idea. It currently has only one contributor. VerdanTech has been built with (sentientist values)[https://sentientism.info/] in mind, and as such does not consider sentient beings as acceptable subjects of exploitation for food or any other purpose.

The application is intended to be built for as many use cases as possible, both in the versatility of the model, scalability for large deployments, and ease of use for localized deployments. If you wish to deploy this application yourself, see the (Deployment)[] section. If the instructions are not adequate in guiding you to a successful deployment, please reach out for assistance and suggestions for improvements to the workflow. 

The key technical features of VerdanTech are:
1. The backend is an asyncronous python HTTP and websocket application, using the (Litestar)[] ASGI framework for API, Posgresql for persisted model state, Redis for in-memory model state, a (differential synchronization)[] algorithm for multi-client synchronization, and a clean architecture with core domain logic in pure Python.
2. The frontend is a SvelteKit application configured in static adapter (pure SPA) mode, using (Orval)[] for client generation with (Svelte Query) and Tailwind + (Skeleton UI)[] for UI/UX. 

Table of contents

## Intro

The intro will contain: the problem this project is trying to solve. The 

VerdanTechs

What's the problem? 

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

## Roadmap

### Completed

### In progress

- User management system

### Planned

- Garden creation and social features

- Workspace creation and planting area definition

- Plant type and variety functionality

- Planting scheme creation, switching between, etc

- Plant instance planting, pulling, deleting, forecasting, change of forcasting based on new input data

- Differential synchronization

- Bulk planting 

- Rolling planting scheme generation

- Actions output

## Media

youtube channel
totalveganic futurism



# Deployment

There are two ways to deploy: manual mode on linux and docker mode. Even if you don't know docker I recommend it more cause its easy with docker desktop. More likely you want to run this on a raspbery pi and it's easy there two. But idk how you would manually install tihs on non-linux

# Built With

* [![Svelte][Svelte.dev]][Svelte-url]

# The Codebase

## Repository Structure

The application implements a decoupled backend/frontent arhitecture. The backend is an asynchronous python3.11 running on uvicore, and the frontend is a SvelteKit spa-mode static file generator with Skeleton UI.

## Download and Installation

Recommended VS code theme: Solarized Dark

## Backend

### Background and Architecture

The python backend implements a clean architecture pattern, meaning that the functions of the application are segregated in a way that minimizes coupling. Quick summaries for the layers:
- The domain layer holds the core business logic and is made up of four components: Entities, which are objects with IDs and individuality that represent concepts in the problem space, RootEntities which are entities that make up Collections of documents or SQL tables in the database, meaning they represent consistency boundaries of data, value objects, which are ID-less and immutable, and represent individual-less states, and services, which encapsulate core logic in the problem domain that can't be relegated to any of the other options. All these concepts are implemented using native Python dataclasses. The domain layer also holds interfaces that are relied upon by the domain layer and application layer
- The application layer orchestrates the domain layer and connects it to implementations of the interfaces. The application layer has two parts: the operaions sections, which are high level application functions and make up the main API (are-one to one with http API routes), and the services sections, which comprise more granular orchestrations of the domain logic and are called in the operations.
- The infrastrure contains implementations of the domain service interfaces, such as database implementations of the repository interface. The only repository in use so far is a MongoDB Motor (async pymongo) implementation. The repository abstraction makes it possible to use different implementations in the future, but I havent investigated the potential compatibility with a sql database (plan to stick with mongo)
- The API layer is the http and websocket wrapping around the application layer, and is implemented using the Litestar 

### Documentation

### Contributing

## Frontend

### Background and Architecture

Why I chose Svelte and Skeleton.

### Documentation

### Contributing

# Contributors


# Old draft:
This is the home repository for the VerdanTech web application - an application striving towards creating software tools to automate gardening in a collaborative way - including planning, tracking, optimizing, and automating growing plants. This project is still in its early stages and lacks documentation. You can see the previous version of this project (here)[https://github.com/nathanielarking/Autonomous-Agriculture].

In terms of infrastructure, the project aims to create a REST api using Django Rest Framework, and a frontend Svelte SPA.

Eventually, the application will be integrated with embedded automation projects. Those have a seperate repository, which you can find (here)[https://github.com/nathanielarking/VerdanTech-Devices/tree/main/VerdanTech%20Drip%2