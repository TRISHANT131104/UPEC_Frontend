import React, { createContext, useState } from 'react'
import Cookies from 'js-cookie';


const HomeContext = createContext();
export const HomeProvider = ({children})=>{
  const [auth,setauth] = useState({user:{id:Cookies.get('id')?parseInt(Cookies.get('id')):155,username:Cookies.get('username')?Cookies.get('username'):"barbara16",last_login:"",email:"rpkiit2022@gmail.com"},"access_token":"","refresh_token":""})
  const [EachUsersMessages,setEachUsersMessages] = useState([])
  const [SelectedName,setSelectedName] = useState(false)
  const [Group,setGroup] = useState(false)
  const [Receiver,setReceiver] = useState(null)
  const [AI,setAI] = useState(false)
  const ContextData = {
    auth,
    setauth,
    EachUsersMessages,
    setEachUsersMessages,
    SelectedName,
    setSelectedName,
    Group,
    setGroup,
    Receiver,
    setReceiver,
    AI,
    setAI,
  }
  return (
    <HomeContext.Provider value={ContextData}>
      {children}
    </HomeContext.Provider>
  )
}
export default HomeContext