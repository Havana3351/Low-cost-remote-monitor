const state = {
    personalName: {
        information: '用户名：',
        content: '王小虎'
    },
    personalPhone: {
        information: '电话号码：',
        content: '王小虎'
    },
    personalCom: {
        information: '所属单位：',
        content: '王小虎'
    },
    personalSsl: {
        information: '宿舍楼号：',
        content: '王小虎'
    },
    personalSsh: {
        information: '宿舍号：',
        content: '王小虎'
    },
    personalVideo: {
        information: '视频源：',
        content: '王小虎'
    },
    personalTemp: {
        information: '温度源：',
        content: '王小虎'
    },
    personalHumi: {
        information: '湿度源：',
        content: '王小虎'
    }
}

const mutations = {
    setPersonalName(state, PersonalName){
        state.personalName =PersonalName;
    },
    setPersonalPhone(state, PersonalPhone){
        state.personalPhone = PersonalPhone;
    },
    setPersonalCom(state, PersonalCom){
        state.personalCom = PersonalCom;
    },
    setPersonalSsl(state, PersonalSsl){
        state.personalSsl = PersonalSsl;
    },
    setPersonalSsh(state, PersonalSsh){
        state.personalSsh = PersonalSsh;
    },
    setPersonalVideo(state, PersonalVideo){
        state.personalVideo = PersonalVideo;
    },
    setPersonalTemp(state, PersonalTemp){
        state.personalTemp = PersonalTemp;
    },
    setPersonalHumi(state, PersonalHumi){
        state.personalHumi = PersonalHumi;
    },
    setPersonalPhone1(state, PersonalPhone1){
        state.personalPhone.content = PersonalPhone1;
    },
    setPersonalCom1(state, PersonalCom1){
        state.personalCom.content = PersonalCom1;
    },
    setPersonalSsl1(state, PersonalSsl1){
        state.personalSsl.content = PersonalSsl1;
    },
    setPersonalSsh1(state, PersonalSsh1){
        state.personalSsh.content = PersonalSsh1;
    },
    setPersonalVideo1(state, PersonalVideo1){
        state.personalVideo.content = PersonalVideo1;
    },
    setPersonalTemp1(state, PersonalTemp1){
        state.personalTemp.content = PersonalTemp1;
    },
    setPersonalHumi1(state, PersonalHumi1){
        state.personalHumi.content = PersonalHumi1;
    }
}

const getters = {
    getDataValue: state => {
        return state.dataValue;
    },
    getPersonalTab: state => {
        var personaltable = [state.personalName,state.personalPhone,state.personalCom
            ,state.personalSsl,state.personalSsh,state.personalVideo,state.personalTemp,state.personalHumi];
        return personaltable;
    }
}


export default {
    namespaced: true,
    state,
    getters,
    mutations
}