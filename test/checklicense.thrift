struct ProcessProfile{
        1:i32 process_id,
        2:string c_id,
        3:string process_type
}  
service ProcessCheckL{
        void store(1: ProcessProfile process), 
        ProcessProfile get(1: i32 process_id),
	i32 CheckLicense()
}
