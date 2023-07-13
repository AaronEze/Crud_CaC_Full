const {createApp} = Vue;

createApp({
    data(){
        return{
            contenidos: [],
            url: 'http://127.0.0.1:5000/contenidos',
            cargando: true,
            error: false
        }
    },

    methods: {
        fetchApi(url){
            fetch(url)
            .then(res=>res.json())
            .then(data=>{
                this.contenidos = data;
                this.cargando = false;
            })
            .catch(err=>{
                console.error(err);
                this.error = true;
            })
        },

        eliminar(id){
            const url = 'http://127.0.0.1:5000/contenidos/' + id
            let options = {
                method: 'DELETE'
            } 

            fetch(url, options)
            .then(res => res.json())
            .then(data =>{
                
                location.reload();
            })
            .catch(er=> console.error(err));
        }
    },

    created(){
        this.fetchApi(this.url);
    }
}).mount('#app')