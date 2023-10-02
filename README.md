# VerdanTech - The Collaborative Garden Productivity Tool

Intro

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

## License

gnu gpl 3.0

# Deployment

There are two ways to deploy: manual mode on linux and docker mode. Even if you don't know docker I recommend it more cause its easy with docker desktop. More likely you want to run this on a raspbery pi and it's easy there two. But idk how you would manually install tihs on non-linux

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

# Extended Project


# Old draft:
This is the home repository for the VerdanTech web application - an application striving towards creating software tools to automate gardening in a collaborative way - including planning, tracking, optimizing, and automating growing plants. This project is still in its early stages and lacks documentation. You can see the previous version of this project (here)[https://github.com/nathanielarking/Autonomous-Agriculture].

In terms of infrastructure, the project aims to create a REST api using Django Rest Framework, and a frontend Svelte SPA.

Eventually, the application will be integrated with embedded automation projects. Those have a seperate repository, which you can find (here)[https://github.com/nathanielarking/VerdanTech-Devices/tree/main/VerdanTech%20Drip%2