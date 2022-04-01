<template>
    <div>
        <NavMenu></NavMenu>
        <Breadcrumb id="Breadcrumb"></Breadcrumb>
        <Avatar id="Avatar"></Avatar>
        <el-divider id="divider1"></el-divider>
        <personal></personal>
    </div>
</template>

<script>
    import Breadcrumb from '../../components/Breadcrumb.vue'
    import Personal from '../../components/Person/PersonalInfo.vue'
    import NavMenu from '../../components/NavMenu.vue'
    import Avatar from "../../components/Avatar"
    import {getCookie} from '../../cookie.js'
    import store from '../../store/index.js'

    export default{
        components: {
            Breadcrumb,
            Personal,
            NavMenu,
            Avatar
        },
        data(){
            return {
                info: {}
            }
        },
        mounted: function(){
            var username = getCookie('username');
            this.$axios.get('http://47.95.11.87/api/profile',{
                params: {
                    username: username
                }
            })
            .then(//response=> (this.info = response)
                function (response) {
                    console.log(response);
                    if(response != null){
                        console.log(response.data.name);
                        store.commit('personal/setPersonalName',response.data.name);
                        store.commit('personal/setPersonalPhone',response.data.phone);
                        store.commit('personal/setPersonalCom',response.data.campus);
                        store.commit('personal/setPersonalSsl',response.data.dorm);
                        store.commit('personal/setPersonalSsh',response.data.room);
                        store.commit('personal/setPersonalVideo',response.data.video);
                        store.commit('personal/setPersonalTemp',response.data.temp);
                        store.commit('personal/setPersonalHumi',response.data.humi);
                    }
                })
                .catch(function (error) { // 请求失败处理
                    console.log(error);
                });

        }
    }

</script>

<style scoped>
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
</style>