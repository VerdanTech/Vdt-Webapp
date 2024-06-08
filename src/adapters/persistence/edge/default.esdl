module common {
    abstract type Entity {
        
    }

    abstract type RootEntity extending Entity {

    }

    abstract type ValueObject {

    }

    abstract type Ref {
        required id: uuid; 
    }
}