#!/usr/bin/env ruby
#Matching string
input = ARGV[0]

if input.match(/School/)
  puts input.match(/School/)[0]
else
  puts ""
end

