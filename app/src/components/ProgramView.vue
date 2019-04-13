<template>
    
    <div>
        <div v-for="card in program" v-bind:key="card.card_number">
        <div v-if="card != null">
            <CardView 
                :card-number="card.card_number"
                :card-type="card.card_type"
                :display="card.display"
                :color="card.card_color"
                :inserted="inserted"
                :current="current"
                >
            </CardView>

            <CardView 
                :card-number="card.external_dependant.card_number"
                :card-type="card.external_dependant.card_type"
                :display="card.external_dependant.display"
                :color="card.external_dependant.card_color"
                :inserted="inserted"
                :current="current"
                >
            </CardView>
        </div>

            <div v-if="card.children != null" class="indented">
            <ProgramView
                :program="card.children"
                :inserted="inserted"
                :current="current">
            </ProgramView>
            </div>
        </div>
    </div>


</template>

<script>
import CardView from '@/components/CardView.vue';

export default {
    name: 'ProgramView',
    props: {
        program: Array,
        inserted: Number,
        current: Number,
    },
    components:{
        CardView,
    }
}
</script>

<style lang="scss" scoped>

    $color1 : #7E7F9A;
    $color2 : #EB9486;
    $color3 : #F3DE8A;
    $color4 : #272838;
    $color5 : #F9F8F8;

    .indented{
    /* display: inline-block; */
    padding-left: 10px;
    border-left: 70px solid $color1;
    /* border-bottom: 5px outset #555; */
    }
</style>
