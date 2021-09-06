function BatteryStatus{
    param([string] $computer)

    $BatteryStatus = (Get-WmiObject -class win32_battery -ComputerName $computer).BatteryStatus # Check if batterry is being charging or not 
        
    if($BatteryStatus -eq 2){ # status = 1 --> battery is not being charged || 2 --> battery is being charged
        :test while($BatteryStatus -lt "100"){
            $ChargeRemaining = (Get-WmiObject -class win32_battery -ComputerName $computer).EstimatedChargeRemaining
            
            if($ChargeRemaining -eq "100"){
                $msg = [System.Windows.Forms.MessageBox]::Show("Full charged battery","Advice",[System.Windows.Forms.MessageBoxButtons]::OK) # Display message box to user
                
                break test #end while loop
            }
            
            sleep -Seconds 900 # Script will sleep 15 minutes
        }
    }
}


$computer = "localhost"
BatteryStatus($computer)