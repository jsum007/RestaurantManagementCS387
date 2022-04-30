import React,{Component} from 'react';
import Home from '../Home/Home';
import Menu from '../Menu/Menu';
import Order from '../OrderOnline/OrderOnline';
import Cart from '../Cart/Cart';
import Login from '../../Components/navigation/login/login'
import SignIn from '../../Components/navigation/login/signin'
import {Switch,Route,Router, BrowserRouter} from 'react-router-dom';
import Offer from '../Offer/Offer';
import Chef from '../../Components/staff/chef/chef.js';
import axios from 'axios';
import ForLoad from '../../Components/miscelleous/forLoad';
import LoginStaff from '../../Components/navigation/login/staff/loginStaff'
import Chef_preparing from '../../Components/staff/chef/chef_preparing';
import Chef_history from '../../Components/staff/chef/chef_history';
import Manager from '../../Components/staff/manager/manager';
import Waiter from '../../Components/staff/waiter/waiter';
import Menu_north from '../../Components/menuSections/menu_north';
import Menu_south from '../../Components/menuSections/menu_south';
import Menu_east from '../../Components/menuSections/menu_east';
import Menu_west from '../../Components/menuSections/menu_west';
import Menu_central from '../../Components/menuSections/menu_central';
class allClass extends Component{
    state={
        item:[],
        data:[],
        loaded:false
      };
      componentDidMount(){
        axios.get("https://twobrother0927.firebaseio.com/.json").then((data)=>{
            var t={...data.data,menu:{north:{Gajar_ka_halwa:{image:"https://i2.wp.com/kalimirchbysmita.com/wp-content/uploads/2016/01/Gajar-ka-Halwa-03-1024x683.jpg?resize=1024%2C683",
            price:	454},Jalebi	:{image:"https://images.indianexpress.com/2020/04/jalebis-759.jpg",price:	423},Lassi	:{image:"http://thepinchoftaste.com/assets/images/blogs/Lassi__2021_05_11_06_06_25.jpeg",price:	561},
            Petha	:{image:"https://img-global.cpcdn.com/recipes/80884fdf122d2cc1/1200x630cq70/photo.jpg",price:	414},
            Rabri	:{image:"https://i2.wp.com/www.flavoursonplate.com/wp-content/uploads/2018/12/rabdi-recipe-3.jpg?fit=1200%2C800&ssl=1",price:	526},
            Singori	:{image:"https://upload.wikimedia.org/wikipedia/commons/b/bd/Singori.jpg",price:	508},Sohan_halwa	:{image:"https://www.foodfeasta.com/userdata/public/gfx/d3db2cdcccad229b51b0f3a6df0c8ebd.jpg",price:	478},Malapua	:{image:"https://www.cookwithmanali.com/wp-content/uploads/2018/02/Malpua-500x375.jpg",price:	426}
            ,Aloo_gobi	:{image:"https://www.indianhealthyrecipes.com/wp-content/uploads/2022/03/aloo-gobi-recipe-500x375.jpg",price:	588},Aloo_tikki	:{image:"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvAOoSF8iYSbh7jk7PEI2psCBQGgauK7ZTxw&usqp=CAU",price:	581}
            ,Aloo_matar	:{image:"https://www.cookwithmanali.com/wp-content/uploads/2018/05/Instant-Pot-Aloo-Matar-500x500.jpg",price:	509},Aloo_methi	:{image:"https://www.cookwithmanali.com/wp-content/uploads/2019/04/Aloo-Methi.jpg",price:	516},
            Aloo_shimla_mirch	:{image:{},price:	485},Bhatura	:{image:{},price:	585}
            ,Bhindi_masala	:{image:{},price:	548},Butter_chicken	:{image:{},price:	422},Chana_masala	:{image:{},price:	446}
            ,Chicken_Tikka_masala	:{image:{},price:	489},Chicken_Tikka	:{image:{},price:	502},Chole_bhature	:{image:{},price:	561}
            ,Dal_makhani 	:{image:{},price:	432},Dal_tadka	:{image:{},price:	593},Dum_aloo	:{image:{},price:	479}
            ,Kachori	:{image:{},price:	428},Kadai_paneer	:{image:{},price:	511},Kadhi_pakoda	:{image:{},price:	408}
            ,Karela_bharta	:{image:{},price:	464},Kofta	:{image:{},price:	444}
            ,Lauki_ke_kofte	:{image:{},price:	479},Litti_chokha	:{image:{},price:	411}
            ,Makki_di_roti_sarson_da_saag	:{image:{},price:	478},Misi_roti	:{image:{},price:	422}
            ,Mushroom_do_pyaza	:{image:{},price:	572},Mushroom_matar	:{image:{},price:	556}
            ,Naan	:{image:{},price:	576},Navrattan_korma	:{image:{},price:	412},Palak_paneer	:{image:{},price:	454},
            Paneer_butter_masala	:{image:{},price:	555},Paneer_tikka_masala	:{image:{},price:	529}
            ,Paratha	:{image:{},price:	458},Pindi_chana	:{image:{},price:	593}
            ,Rajma_chaval	:{image:{},price:	470},Rongi	:{image:{},price:	465}
            ,Sattu_ki_roti	:{image:{},price:	586},Shahi_paneer	:{image:{},price:	554}
            ,Vegetable_jalfrezi	:{image:{},price:	536},Tandoori_Chicken	:{image:{},price:	461}
            ,Tandoori_Fish_Tikka:{image:{},price:	528},Shufta	:{image:{},price:	470}}
            ,south:{Ariselu	:{image:{},price:	529},Bandar_laddu	:{image:{},price:	417}
            ,Dharwad_pedha	:{image:{},price:	412},Double_ka_meetha	:{image:{},price:	420}
            ,Gavvalu	:{image:{},price:	576},Kakinada_khaja	:{image:{},price:	406}
            ,Kuzhi_paniyaram	:{image:{},price:	493},Mysore_pak	:{image:{},price:	542}
            ,Obbattu_holige	:{image:{},price:	575},Palathalikalu	:{image:{},price:	579}
            ,Poornalu	:{image:{},price:	534},Pongal	:{image:{},price:	513},Pootharekulu	:{image:{},price:	494}
            ,Qubani_ka_meetha	:{image:{},price:	588},Sheer_korma	:{image:{},price:	423}
            ,Unni_Appam	:{image:{},price:	502},Kajjikaya	:{image:{},price:	532}
            ,Biryani	:{image:{},price:	513},Shahi_tukra	:{image:{},price:	548},
            Attu	:{image:{},price:	419},Avial	:{image:{},price:	514},Bisi_bele_bath	:{image:{},price:	430},
            Currivepillai_sadam 	:{image:{},price:	494},Dosa	:{image:{},price:	473}
            ,Idiappam	:{image:{},price:	440},Idli	:{image:{},price:	471},
            Kanji	:{image:{},price:	504},Kaara_kozhambu	:{image:{},price:	549}
            ,Keerai_kootu	:{image:{},price:	444},Keerai_masiyal	:{image:{},price:	409}
            ,Keerai_sadam	:{image:{},price:	592},Keerai_poriyal	:{image:{},price:	586}
            ,Beef_Fry	:{image:{},price:	447},Kootu	:{image:{},price:	519}
            ,Kos_kootu	:{image:{},price:	507},Koshambri	:{image:{},price:	547}
            ,Kothamali_sadam	:{image:{},price:	447},Kuzhakkattai	:{image:{},price:	483}
            ,Kuzhambu	:{image:{},price:	516},Masala_Dosa	:{image:{},price:	515},Pachadi	:{image:{},price:	572}
            ,Paniyaram	:{image:{},price:	414},Papadum	:{image:{},price:	579}
            ,Paravannam	:{image:{},price:	487},Payasam	:{image:{},price:	420}
            ,Paruppu_sadam	:{image:{},price:	499},Pesarattu	:{image:{},price:	470}
            ,Poriyal	:{image:{},price:	531},Puli_sadam	:{image:{},price:	452}
            ,Rasam	:{image:{},price:	499},Puttu	:{image:{},price:	526}
            ,Sambar	:{image:{},price:	580},Sandige	:{image:{},price:	438}
            ,Sevai	:{image:{},price:	427},Thayir_sadam	:{image:{},price:	465}
            ,Theeyal	:{image:{},price:	496},Uttapam	:{image:{},price:	596}
            ,Vada	:{image:{},price:	588},Chicken_Varuval	:{image:{},price:	426}}
            ,east:{Balu_shahi	:{image:{},price:	596},Gulab_jamun	:{image:{},price:	516}
            ,Imarti	:{image:{},price:	449},Kalakand	:{image:{},price:	438}
            ,Phirni	:{image:{},price:	574},Chhena_jalebi	:{image:{},price:	554}
            ,Chhena_kheeri	:{image:{},price:	510},Chhena_poda	:{image:{},price:	600}
            ,Cham_cham	:{image:{},price:	413},Kheer_sagar	:{image:{},price:	486}
            ,Ledikeni	:{image:{},price:	575},Lyangcha	:{image:{},price:	545}
            ,Mihidana	:{image:{},price:	452},Misti_doi	:{image:{},price:	449}
            ,Pantua	:{image:{},price:	483},Pithe	:{image:{},price:	420}
            ,Rasabali	:{image:{},price:	568},Ras_malai	:{image:{},price:	542}
            ,Rasgulla	:{image:{},price:	406},Sandesh	:{image:{},price:	536}
            ,Adhirasam	:{image:{},price:	469},Maach_Jhol	:{image:{},price:	532}
            ,Pork_Bharta	:{image:{},price:	400},Chak_Hao_Kheer	:{image:{},price:	474}
            ,Galho	:{image:{},price:	419},Chicken_razala	:{image:{},price:	521}
            ,Daal_puri	:{image:{},price:	423},Cheera_Doi	:{image:{},price:	431}
            ,Gheela_Pitha	:{image:{},price:	527},Khar	:{image:{},price:	424}
            ,Kumol_Sawul	:{image:{},price:	427},Luchi	:{image:{},price:	498}
            ,Alu_Pitika	:{image:{},price:	504},Masor_tenga	:{image:{},price:	429}
            ,Bengena_Pitika	:{image:{},price:	435},Bilahi_Maas	:{image:{},price:	455}
            ,Black_rice	:{image:{},price:	523},Bora_Sawul	:{image:{},price:	517}
            ,Chingri_malai_curry	:{image:{},price:	476},Goja	:{image:{},price:	445}
            ,Hando_Guri	:{image:{},price:	598},Haq_Maas	:{image:{},price:	565},
            Chingri_Bhape	:{image:{},price:	556},Kabiraji	:{image:{},price:	568}
            ,Khorisa	:{image:{},price:	447},Koldil_Chicken	:{image:{},price:	447},Konir_Dom	:{image:{},price:	474}
            ,Koldil_Duck	:{image:{},price:	523},Masor_Koni	:{image:{},price:	465}
            ,Mishti_Chholar_Dal	:{image:{},price:	568},Pakhala	:{image:{},price:	410}
            ,Pani_Pitha	:{image:{},price:	437},Payokh	:{image:{},price:	516},Prawn_malai_curry	:{image:{},price:	477}
            ,Shukto	:{image:{},price:	537},Til_Pitha	:{image:{},price:	473}}
            ,west:{Boondi	:{image:{},price:	586},Ghevar	:{image:{},price:	599},Sheera	:{image:{},price:	567}
            ,Sohan_papdi	:{image:{},price:	556},Chikki	:{image:{},price:	479},Anarsa	:{image:{},price:	454}
            ,Basundi	:{image:{},price:	573},Dhondas	:{image:{},price:	431},Doodhpak	:{image:{},price:	484}
            ,Mahim_halwa	:{image:{},price:	473},Modak	:{image:{},price:	432},Shankarpali	:{image:{},price:	572}
            ,Shrikhand	:{image:{},price:	580},Sutar_feni	:{image:{},price:	560},Chapati	:{image:{},price:	555}
            ,Daal_baati_churma	:{image:{},price:	416},Poha	:{image:{},price:	489},Pattor	:{image:{},price:	589},Amti	:{image:{},price:	434}
            ,Zunka	:{image:{},price:	518},Kolim_Jawla	:{image:{},price:	588},Saath	:{image:{},price:	506}
            ,Bajri_no_rotlo	:{image:{},price:	467},Coconut_vadi	:{image:{},price:	515}
            ,Bhakri	:{image:{},price:	463},Bombil_fry	:{image:{},price:	466},Chakali	:{image:{},price:	554}
            ,Chevdo	:{image:{},price:	531},Chorafali	:{image:{},price:	480},Copra_paak	:{image:{},price:	520},Daal_Dhokli	:{image:{},price:	522}
            ,Kutchi_dabeli	:{image:{},price:	514},Dahi_vada	:{image:{},price:	590},Dalithoy	:{image:{},price:	559},Dhokla	:{image:{},price:	457}
            ,Dudhi_halwa	:{image:{},price:	450},Gatta_curry	:{image:{},price:	418},Gud_papdi	:{image:{},price:	446},Ghooghra	:{image:{},price:	422},Handwo	:{image:{},price:	436},Halvasan	:{image:{},price:	443}
            ,Jeera_Aloo	:{image:{},price:	507},Kansar	:{image:{},price:	539},Keri_no_ras	:{image:{},price:	449},Khakhra	:{image:{},price:	498}
            ,Khandvi	:{image:{},price:	526},Kombdi_vade	:{image:{},price:	592},Koshimbir	:{image:{},price:	491},Methi_na_Gota	:{image:{},price:	515}
            ,Mohanthal	:{image:{},price:	564},Muthiya	:{image:{},price:	410},Patra	:{image:{},price:	582},Pav_Bhaji	:{image:{},price:	465}
            ,Puri_Bhaji	:{image:{},price:	543},Sabudana_Khichadi	:{image:{},price:	518},Sev_khamani	:{image:{},price:	569},Sev_tameta	:{image:{},price:	562}
            ,Namakpara	:{image:{},price:	588},Sukhdi	:{image:{},price:	411},Surnoli	:{image:{},price:	514},Thalipeeth	:{image:{},price:	527}
            ,Undhiyu	:{image:{},price:	521},Veg_Kolhapuri	:{image:{},price:	425},Vindaloo	:{image:{},price:	436},Lilva_Kachori	:{image:{},price:	433},Mag_Dhokli	:{image:{},price:	561}
            ,Khichu	:{image:{},price:	524},Thepla	:{image:{},price:	549},Farsi_Puri	:{image:{},price:	565},Khaman	:{image:{},price:	475},Turiya_Patra_Vatana_sabji	:{image:{},price:	572}
            ,Churma_Ladoo	:{image:{},price:	570},Bebinca	:{image:{},price:	465},Pinaca	:{image:{},price:	472}},central:{Fara:{image:{},price:538}, Laapsi:{image:{},price:514},Mawa_Bati:{image:{},price:431}}}}
            console.log(data.data.menu);
            this.setState({data:t,loaded:true});
            
        }).catch(err=>console.log("Some Error")).then(console.log("Lets trye this "));
      }
      addItem=(obj)=>{
          let extra=[...this.state.item];
          var check=false;
          extra.forEach(element=>{
              if(element.head===obj.head){
                check=true;  
                element.counter+=1;
              }

          });
          if(!check){
            extra.push(obj);
          }
          
          this.setState({item:extra});
          
          alert(`${obj.head} is added to your cart`);
      }
      removeItem=(obj)=>{
        var copy=[...this.state.item];
        var check=false;
        let pos=-1;
        copy.forEach(element=>{
            
            if(element.head===obj.head && element.counter>=1 ){
                element.counter=element.counter-1;
                check=true;
            }
            pos+=1;
        });
        if(check){
            
            if(copy[pos].counter===0){
                copy=copy.slice(0,pos).concat(copy.slice(pos+1));
                
            }
        }
        this.setState({item:copy});
        
      }
      
    render(){
        
        const ddt=this.state.loaded?(
            <div>
            <BrowserRouter>
            <Switch>
            <Route path="/chef_history/:id" component={()=><Chef_history/>}/>
            <Route path="/chef_preparing/:id" component={()=><Chef_preparing/>}/>
            <Route path="/chef/:id" component={()=><Chef/>}/>
            <Route path="/manager/:id" component={()=><Manager/>}/>
            <Route path="/waiter/:id" component={()=><Waiter/>}/>
            <Route path="/offers" component={()=><Offer count={this.state.item.length} data={this.state.data.offers.offer} board={this.state.data.offers.board}/>}/>
            <Route path="/cart" component={()=><Cart adding={()=>this.addItem} remove={()=>this.removeItem} data={this.state.item}/> }/>
            <Route path="/menu_north" component={()=><Menu_north/>}/>
            <Route path="/menu_south" component={()=><Menu_south/>}/>
            <Route path="/menu_east" component={()=><Menu_east/>}/>
            <Route path="/menu_west" component={()=><Menu_west/>}/>
            <Route path="/menu_central" component={()=><Menu_central/>}/>
            <Route path="/menu" component={()=><Menu inbox={this.state.item.length} data={this.state.data.menu} loaded={this.state.loaded} adding={()=>this.addItem}/>}/>
            <Route path="/order" component={()=><Order count={this.state.item.length} data={this.state.item}/>}/>
            <Route path="/login_/sign-in" component={()=><SignIn/>}/>
            <Route path="/login_" component={()=><Login/>}/>
            <Route path="/login_staff" component={()=><LoginStaff/>}/>
            <Route path="/" component={()=><Home count={this.state.item.length} data={this.state.data.offers.home}/>}/>
   </Switch>
   </BrowserRouter>
       </div>
        ):<ForLoad/>;
        return(
           ddt
        );
    }
}

export default allClass;

