<template>
        <div :class="['ge-card', 'has-text-weight-bold', 
        {tt:cardType[0]},
        {bt:cardType[1]},
        {lp:cardType[2]},
        {rp:cardType[3]},
        {lh:cardType[4]},
        {rh:cardType[5]},
        color,
        ]">
            <span class="card-number">{{ cardNumber }}</span>
            <span v-for="element in display" :key="element">
                <span v-if="element.val_type === 'text'">
                    {{ element.text }} &nbsp;
                </span>
                <div class="sticker" v-else-if="element.val_type === 'sticker'">
                    {{ element.sticker_name }} &nbsp;<i class="fas fa-equals"></i>
                    <span class="sticker-val">
                        {{ element.sticker_value }}
                    </span>
                </div>
                <span v-if="element.val_type === 'internal_dependant'">
                    <CardView 
                        :card-number="element.dependant.card_number"
                        :card-type="element.dependant.card_type"
                        :display="element.dependant.display"
                        :color="element.dependant.card_color">
                    </CardView>
                </span>
            </span>

        </div>
</template>

<script>
export default {
    name: 'CardView',
    mounted() {
        let recaptchaScript = document.createElement('script');
        recaptchaScript.setAttribute('src', 'https://use.fontawesome.com/releases/v5.3.1/js/all.js');
        document.head.appendChild(recaptchaScript);
    },
    props: {
        cardNumber: Number,
        cardType: Array,
        display: Array,
        color: String,
    },
}
</script>

<style lang="scss" scoped>

    $color1 : #7E7F9A;
    $color2 : #EB9486;
    $color3 : #F3DE8A;
    $color4 : #272838;
    $color5 : #F9F8F8;

    $color_logic : darkblue;
    $color_condition :yellow;

    .color_normal{
        background-color: $color1;
    }

    .color_condition{
        background-color: $color1;
    }
    .color_logic{
        background-color: $color1;
    }
    .color_math{
        background-color: $color1;
    }

    .color_internal{
        background-color: $color4;
    }

    .ge-card{
        // display: inline-block;
        color: $color5;
        padding: 5px 5px;
        border-radius: 5px 5px 5px 0px;
        position: relative;
        height: 100%;
        margin-right: 5px;
        float: left;
    }

    .tt{
    border-top: 5px outset #555;
    }
    .bt{
    border-bottom: 5px outset #555;
    }

    .rp:after{
    left: 100%;
    top: 50%;
    border: solid transparent;
    content: " ";
    height: 0;
    width: 0;
    position: absolute;
    pointer-events: none;
    border-color: rgba(136, 183, 213, 0);
    border-left-color: $color1;
    border-width: 10px;
    margin-top: -10px;
    }

    .rh:after{
    right: 0%;
    top: 50%;
    border: solid transparent;
    content: " ";
    height: 0;
    width: 0;
    position: absolute;
    pointer-events: none;
    border-color: hsla(203, 48%, 68%, 0);
    border-right-color: white;
    border-width: 10px;
    margin-top: -10px;
    }

    // .lp{
    //     margin-left: 3px;
    // }

    .lp:before {
    right: 100%;
    top: 50%;
    border: solid transparent;
    content: " ";
    height: 0;
    width: 0;
    position: absolute;
    pointer-events: none;
    border-color: rgba(136, 183, 213, 0);
    border-right-color: $color1;
    border-width: 10px;
    margin-top: -10px;
    }

    .lh:before {
    left: 0%;
    top: 50%;
    border: solid transparent;
    content: " ";
    height: 0;
    width: 0;
    position: absolute;
    pointer-events: none;
    border-color: rgba(136, 183, 213, 0);
    border-left-color: white;
    border-width: 10px;
    margin-top: -10px;
    }

    .sticker{
    display: inline-block;  
    background-color: $color3;
    color: $color4;
    padding: 5px;
    margin-right: 7px;
    border-radius: 5px;
    }

    .end{
    position: relative;
    right:-5px;
    }

    .sticker-val{
    background-color: $color2;
    color: $color4;
    padding: 5px;
    margin: 2px;
    border-radius: 5px;
    }

    .card-number{
    background-color: $color5;
    color: $color4;
    border-radius: 50%;
    padding: 7px;
    margin: 10px;
    }
</style>
