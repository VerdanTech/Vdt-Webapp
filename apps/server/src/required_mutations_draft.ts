import {co, Group} from "jazz-tools"
import { GardenIndexSchema, GLOBAL_COVAL_ID_PUBLIC_GARDEN_INDEX } from '../../../packages/models/src/gardens/schema';

const globalIndexGroup = Group.create()
globalIndexGroup.addMember("everyone", "reader")


async function initializeGardenIndex() {

}

const gardenIndex = await GardenIndexSchema.getOrCreateUnique({
    unique: GLOBAL_COVAL_ID_PUBLIC_GARDEN_INDEX,
    owner: globalIndexGroup
})