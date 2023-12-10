"use client";
import React, { useContext,useRef,useEffect } from 'react'
import { useState } from 'react';
import SenderChatCard from './SenderChatCard';
import { IoSend } from "react-icons/io5";
import RecieverChatCard from './RecieverChatCard';
import HomeContext from '@/context/HomeContext';
import { GoCopilot } from "react-icons/go";
export default function MainChatCard({id}) {
    const {auth,EachUsersMessages, setEachUsersMessages,SelectedName,setSelectedName,Receiver,Group,AI,setAI} = useContext(HomeContext)
    console.log(EachUsersMessages)
    let socket = useRef(null);
    const [message,setmessage] = useState(null)
    useEffect(() => {
      
      socket.current = new WebSocket(
        `ws://127.0.0.1:8000/ws/chat/${auth?.user?.id}`
      );
  
      socket.current.onopen = () => {
        console.log("ws opened");
      };
      socket.current.onmessage = (e) => {
        const data = JSON.parse(e.data);
        console.log(e);
        console.log(data);
        if (data["type"] === "sent_message") {
          console.log(data);
          const new_data = {
            sender: data["sender"],
            message: data["message"],
            receiver: data["receiver"],
            id: data["id"],
            created_at_date: data["created_at_date"],
            created_at_time: data["created_at_time"],
          };
          setEachUsersMessages((prev) => {
            return [...prev, new_data];
          });
        } else if (data["type"] === "receive_message") {
          const new_data = {
            sender: data["sender"],
            message: data["message"],
            receiver: data["receiver"],
            id: data["id"],
            created_at_date: data["created_at_date"],
            created_at_time: data["created_at_time"],
            group:data["group"],
            ai:data["ai"]
          };
          setEachUsersMessages((prev) => {
            return [...prev, new_data];
          });
        }
      };
      socket.current.onclose = () => {
        console.log("ws closed");
      };
      socket.current.onerror = (e) => {
        console.log(e);
      };
  
    }, [socket.current,auth]);
  return (
    <div className='border border-gray-200 bg-white w-3/4 h-screen  relative'>
        <div className="w-full flex items-start justify-start p-2 border border-gray-200 absolute top-0 bg-white z-1">
            <img src="https://www.gravatar.com/avatar/2acfb745ecf9d4dccb3364752d17f65f?s=260&d=mp" alt="" className="w-16 h-16 rounded-full" />
            <div className="flex flex-col px-4 justify-center items-start text-gray-600">
                <h2 className="text-xl">{SelectedName}</h2>
                <h3 className="text-lg">Last active at: 3rd Nov 2023, 7:08PM</h3>
            </div>
        </div>
        <div className="h-screen overflow-scroll py-[100px]">
            {EachUsersMessages?.map((ele)=>{
                return (
                    <div>
                        {ele.sender == auth.user.username ? (
                            <RecieverChatCard ele={ele}/>
                            
                        ):(
                            <SenderChatCard ele={ele}/>
                        )}
                    
                    </div>
                )
            })}
        </div>
        <div className="flex justify-center items-center border border-gray-200 p-4 absolute bottom-0 bg-white w-full">
            <input onChange={(e)=>{
              setmessage(e.target.value)
            }} placeholder="Enter Your Message" className="mx-4 border border-gray-200 h-10 w-full rounded-lg px-2 text-black"/>
            <button className='text-black flex' onClick={()=>{
              
              socket.current.send(JSON.stringify({
                "type":"send_message_to_user",
                "data":{
                  "sender":auth.user.id,
                  "receiver":Receiver,
                  "group":Group,
                  "ai":AI,
                  "message":message
                }
              }))
            }}><IoSend className='text-black mx-4 w-8 h-8'  /> </button>
            {Group && <button id="ai-grp-btn" className='text-black' onClick={(e)=>{
              if(document.getElementById('ai-grp-btn').classList.contains('text-blue-600')){
                setAI(false)
                document.getElementById('ai-grp-btn').className = "text-black"
              }
              else{
                setAI(true)
                document.getElementById('ai-grp-btn').className = "text-blue-600"
              }
              
            }}><GoCopilot  className=' transition-all fade-in-out mx-4 w-8 h-8'  /></button>}
            

      </div>
    </div>
  )
}


const fetchPersonalChats = async (data) => {
    return axios
      .post(
        `http://127.0.0.1:8000/api/v1/__get__personal__chat__/${data.receiver_id}`,
        {id:data.sender_id},
        {
          headers: {
            Authorization: `Bearer ${data.access}`,
          },
        }
      )
      .then((response) => {
        return response.data;
      })
      .catch((error) => {
        console.log(error);
        return [];
      });
  };
  
  const useGetPersonalChats = () => {
    const queryClient = useQueryClient();
    const { EachUsersMessages, setEachUsersMessages } = useContext(HomeContext);
    return useMutation({
      mutationFn: fetchPersonalChats,
      onSuccess: (data) => {
        console.log(data);
        setEachUsersMessages(data);
        queryClient.invalidateQueries(["UsersMessages"]);
      },
      onError: (context) => {
        queryClient.setQueryData(["UsersMessages"], context.previousData);
      },
    });
  };