<template>
    <div>
        <div>
            <NavMenu></NavMenu>
            <Breadcrumb id="Breadcrumb"></Breadcrumb>
            <Avatar id="Avatar"></Avatar>
            <el-divider id="divider1"></el-divider>
        </div>
        <div id="backgroudDiv">
            <div id="ChartHisDiv">
                <el-card id="Chart">
                    <ChartHis></ChartHis>
                </el-card>
            </div>
        </div>
    </div>
</template>

<script>
    import NavMenu from '../../components/NavMenu.vue'
    import Breadcrumb from '../../components/Breadcrumb.vue'
    import Avatar from "../../components/Avatar";
    import ChartHis from "../../components/temhui/ChartHis";
    import {getCookie} from "../../cookie";
    import store from "../../store";

    export default{
        components: {
            NavMenu,
            Breadcrumb,
            Avatar,
            ChartHis
        },
        data(){
            return {
                info: null
            }
        },
        /*beforeCreate: function(){

        }*/
    }
</script>

<style>
    #Breadcrumb{
        margin-top: 20px;
        margin-left: 300px;
    }
    #divider1{
        width: 86%;
        margin-top: 11px;
        margin-left: 244px;
    }
    #Avatar {
        margin-left: 93%;
        margin-top: -27px;
    }
    #backgroudDiv{
        background-color: #eceef1;
        height: 710px;
        margin-top: -1.7%;
    }
    #ChartHisDiv{
        width: 70%;
        margin-left: 23%;
        margin-top: 7%;
        position: absolute;
    }
    #Chart{
        width: 100%;
    }
</style>
